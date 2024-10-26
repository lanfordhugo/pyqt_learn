"""
线程管理示例
展示了如何创建、启动、停止和重启线程
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import time

class ManagedThread(QThread):
    """可管理的工作线程"""
    status = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self._is_running = True
    
    def run(self):
        """线程执行的任务"""
        while self._is_running:
            self.status.emit("工作中...")
            time.sleep(1)
            
    def stop(self):
        """停止线程"""
        self._is_running = False
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("线程管理示例")
        
        # 创建UI
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.status_label = QLabel("就绪")
        self.start_button = QPushButton("启动")
        self.stop_button = QPushButton("停止")
        
        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        
        # 初始化线程
        self.thread = ManagedThread()
        self.thread.status.connect(self.update_status)
        
        # 连接按钮信号
        self.start_button.clicked.connect(self.start_thread)
        self.stop_button.clicked.connect(self.stop_thread)
        
    def start_thread(self):
        """启动线程"""
        if not self.thread.isRunning():
            self._is_running = True
            self.thread = ManagedThread()  # 创建新线程
            self.thread.status.connect(self.update_status)
            self.thread.start()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
    
    def stop_thread(self):
        """停止线程"""
        if self.thread.isRunning():
            self.thread.stop()
            self.thread.wait()  # 等待线程结束
            self.status_label.setText("已停止")
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
    
    def update_status(self, status):
        """更新状态标签"""
        self.status_label.setText(status)
        
    def closeEvent(self, event):
        """窗口关闭时确保线程正确结束"""
        self.stop_thread()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
