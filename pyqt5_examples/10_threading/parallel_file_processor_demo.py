"""
文件: advanced_threading_demo.py
功能: PyQt5多线程综合示例
技术要点:
1. QThread的基本使用
2. QThreadPool和QRunnable的使用
3. 线程状态控制(暂停/恢复/停止)
4. 互斥锁实现线程同步
5. 异常处理和错误传递
6. 多线程数据共享
7. 进度监控和状态更新

实际应用场景：模拟文件处理系统，包含：
- 文件扫描线程
- 文件处理线程池
- 实时进度显示
- 完整的线程控制
"""

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                           QVBoxLayout, QWidget, QLabel, QProgressBar)
from PyQt5.QtCore import (QThread, QThreadPool, QRunnable, QObject, 
                         pyqtSignal, QMutex, QWaitCondition)
import sys
import time
import traceback
import random

class SharedDataManager:
    """共享数据管理器，实现线程安全的数据访问"""
    def __init__(self):
        self.mutex = QMutex()
        self.data = []
        self.processed_count = 0
    
    def add_data(self, item):
        """线程安全的添加数据"""
        self.mutex.lock()
        try:
            self.data.append(item)
        finally:
            self.mutex.unlock()
    
    def get_data(self):
        """线程安全的获取数据"""
        self.mutex.lock()
        try:
            return self.data.pop(0) if self.data else None
        finally:
            self.mutex.unlock()
    
    def increment_processed(self):
        """增加已处理计数"""
        self.mutex.lock()
        try:
            self.processed_count += 1
        finally:
            self.mutex.unlock()

class ScannerThread(QThread):
    """文件扫描线程，模拟文件系统扫描过程"""
    progress = pyqtSignal(int)
    error = pyqtSignal(str)
    finished = pyqtSignal()
    
    def __init__(self, shared_data):
        super().__init__()
        self._is_running = True
        self._is_paused = False
        self.pause_condition = QWaitCondition()
        self.mutex = QMutex()
        self.shared_data = shared_data
        
    def run(self):
        """线程主运行函数，模拟文件扫描过程"""
        try:
            for i in range(100):  # 模拟扫描100个文件
                # 检查暂停状态
                self.mutex.lock()
                if self._is_paused:
                    self.pause_condition.wait(self.mutex)
                self.mutex.unlock()
                
                if not self._is_running:
                    break
                    
                # 模拟文件扫描
                time.sleep(0.1)
                self.shared_data.add_data(f"File_{i}")
                self.progress.emit(i + 1)
                
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

    def pause(self):
        """暂停线程"""
        self._is_paused = True
    
    def resume(self):
        """恢复线程运行"""
        self._is_paused = False
        self.pause_condition.wakeAll()
    
    def stop(self):
        """停止线程"""
        self._is_running = False
        self.resume()  # 确保线程不会卡在暂停状态

class ProcessorSignals(QObject):
    """处理器信号类，用于QRunnable中发送信号"""
    finished = pyqtSignal()
    error = pyqtSignal(str)
    processed = pyqtSignal()

class FileProcessor(QRunnable):
    """文件处理器，使用QRunnable实现并发处理"""
    def __init__(self, shared_data):
        super().__init__()
        self.shared_data = shared_data
        self.signals = ProcessorSignals()
        self._is_running = True
        
    def run(self):
        """处理器主运行函数"""
        try:
            while self._is_running:
                data = self.shared_data.get_data()
                if data is None:
                    time.sleep(0.1)
                    continue
                    
                # 模拟文件处理
                time.sleep(random.uniform(0.1, 0.5))
                self.shared_data.increment_processed()
                self.signals.processed.emit()
                
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit()
    
    def stop(self):
        """停止处理"""
        self._is_running = False

class MainWindow(QMainWindow):
    """主窗口类"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("高级多线程示例")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()
        self.init_threads()
        
    def setup_ui(self):
        """初始化UI界面"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 创建控件
        self.start_button = QPushButton("开始")
        self.pause_button = QPushButton("暂停")
        self.stop_button = QPushButton("停止")
        self.scan_progress = QProgressBar()
        self.process_label = QLabel("已处理: 0 文件")
        
        # 添加控件到布局
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.scan_progress)
        layout.addWidget(self.process_label)
        
        # 初始化按钮状态
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        
        # 连接信号
        self.start_button.clicked.connect(self.start_processing)
        self.pause_button.clicked.connect(self.toggle_pause)
        self.stop_button.clicked.connect(self.stop_processing)
        
    def init_threads(self):
        """初始化线程和线程池"""
        self.shared_data = SharedDataManager()
        
        # 初始化扫描线程
        self.init_scanner()
        
        # 初始化线程池和处理器
        self.thread_pool = QThreadPool()
        self.processors = []
        self.is_paused = False
        
    def init_scanner(self):
        """初始化扫描线程"""
        self.scanner = ScannerThread(self.shared_data)
        self.scanner.progress.connect(self.update_scan_progress)
        self.scanner.error.connect(self.handle_error)
        self.scanner.finished.connect(self.scanning_finished)
    
    def start_processing(self):
        """开始处理"""
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        
        # 启动扫描线程
        self.scanner.start()
        
        # 创建并启动处理器
        for _ in range(3):  # 创建3个处理器
            processor = FileProcessor(self.shared_data)
            processor.signals.processed.connect(self.update_process_count)
            processor.signals.error.connect(self.handle_error)
            self.processors.append(processor)
            self.thread_pool.start(processor)
            
    def toggle_pause(self):
        """切换暂停/继续状态"""
        if not self.is_paused:
            self.scanner.pause()
            self.pause_button.setText("继续")
        else:
            self.scanner.resume()
            self.pause_button.setText("暂停")
        self.is_paused = not self.is_paused
        
    def stop_processing(self):
        """停止所有处理"""
        self.scanner.stop()
        for processor in self.processors:
            processor.stop()
        
        # 等待扫描线程结束
        self.scanner.wait()
        
        # 清空处理器列表
        self.processors.clear()
        
        # 重置UI和数据状态
        self.reset_ui_state()
        self.reset_data()
        
        # 重新初始化扫描线程
        self.init_scanner()
        
        # 重置按钮状态
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        
    def reset_ui_state(self):
        """重置UI状态"""
        self.scan_progress.setValue(0)
        self.process_label.setText("已处理: 0 文件")
        self.pause_button.setText("暂停")
        self.is_paused = False
    
    def reset_data(self):
        """重置数据状态"""
        # 清空共享数据
        self.shared_data.mutex.lock()
        try:
            self.shared_data.data.clear()
            self.shared_data.processed_count = 0
        finally:
            self.shared_data.mutex.unlock()
        
    def update_scan_progress(self, value):
        """更新扫描进度"""
        self.scan_progress.setValue(value)
        
    def update_process_count(self):
        """更新处理计数"""
        self.process_label.setText(f"已处理: {self.shared_data.processed_count} 文件")
        
    def handle_error(self, error_msg):
        """处理错误"""
        print(f"错误: {error_msg}")
        
    def scanning_finished(self):
        """扫描完成处理"""
        print("扫描完成")
        
    def closeEvent(self, event):
        """窗口关闭事件处理"""
        self.stop_processing()
        self.thread_pool.waitForDone()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
