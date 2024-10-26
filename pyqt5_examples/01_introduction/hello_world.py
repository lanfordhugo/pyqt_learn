import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        # 设置窗口标题
        self.setWindowTitle('我的第一个PyQt5应用')
        
        # 创建一个标签
        label = QLabel('你好，世界！', self)
        
        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(label)
        
        # 设置窗口布局
        self.setLayout(layout)
        
        # 设置窗口大小和位置
        self.setGeometry(300, 300, 250, 150)

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建并显示窗口
    window = HelloWorldWindow()
    window.show()
    
    # 运行应用程序的主循环
    sys.exit(app.exec_())
