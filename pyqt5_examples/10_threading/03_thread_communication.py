"""
线程间通信示例
展示了如何使用信号和槽在线程间传递数据
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import time

class DataWorker(QThread):
    """数据处理线程"""
    # 定义多个信号用于不同类型的数据传递
    number_signal = pyqtSignal(int)
    text_signal = pyqtSignal(str)
    data_signal = pyqtSignal(dict)
    
    def run(self):
        """模拟数据处理和传递"""
        # 发送数字
        for i in range(5):
            self.number_signal.emit(i)
            time.sleep(1)
            
        # 发送文本
        self.text_signal.emit("数字处理完成")
        time.sleep(1)
        
        # 发送字典数据
        data = {"status": "完成", "count": 5}
        self.data_signal.emit(data)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("线程通信示例")
        
        # 创建UI
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.number_label = QLabel("数字: -")
        self.text_label = QLabel("文本: -")
        self.data_label = QLabel("数据: -")
        self.start_button = QPushButton("开始")
        
        layout.addWidget(self.number_label)
        layout.addWidget(self.text_label)
        layout.addWidget(self.data_label)
        layout.addWidget(self.start_button)
        
        # 创建工作线程
        self.worker = DataWorker()
        
        # 连接信号和槽
        self.worker.number_signal.connect(self.update_number)
        self.worker.text_signal.connect(self.update_text)
        self.worker.data_signal.connect(self.update_data)
        self.start_button.clicked.connect(self.start_worker)
        
    def start_worker(self):
        """启动工作线程"""
        self.start_button.setEnabled(False)
        self.worker.start()
        
    def update_number(self, value):
        """更新数字显示"""
        self.number_label.setText(f"数字: {value}")
        
    def update_text(self, text):
        """更新文本显示"""
        self.text_label.setText(f"文本: {text}")
        
    def update_data(self, data):
        """更新数据显示"""
        self.data_label.setText(f"数据: {data}")
        self.start_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
