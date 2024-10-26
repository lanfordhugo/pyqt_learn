"""
基础的QThread使用示例
展示了如何创建一个简单的工作线程并与主线程交互
"""

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import time


class WorkerThread(QThread):
    """简单的工作线程"""

    # 定义信号
    counter_value = pyqtSignal(int)

    def run(self):
        """线程执行的任务"""
        for i in range(10):
            time.sleep(1)  # 模拟耗时操作
            self.counter_value.emit(i)  # 发送信号


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread基础示例")

        # 创建UI
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("等待开始...")
        self.button = QPushButton("开始计数")

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # 创建线程
        self.worker = WorkerThread()
        self.worker.counter_value.connect(self.update_label)
        self.button.clicked.connect(self.start_worker)

    def start_worker(self):
        """启动工作线程"""
        self.button.setEnabled(False)
        self.worker.start()

    def update_label(self, value):
        """更新标签显示"""
        self.label.setText(f"当前计数: {value}")
        if value == 9:  # 计数结束
            self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
