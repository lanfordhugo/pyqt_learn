import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("动画框架示例")
        self.setGeometry(100, 100, 600, 400)
        
        # 创建按钮
        self.button = QPushButton("点击我", self)
        self.button.setGeometry(50, 50, 100, 50)
        
        # 创建动画
        self.animation = QPropertyAnimation(self.button, b"geometry")
        self.animation.setDuration(1000)  # 动画持续时间为1000毫秒
        self.animation.setStartValue(QRect(50, 50, 100, 50))
        self.animation.setEndValue(QRect(400, 300, 100, 50))
        
        # 连接按钮点击事件到动画
        self.button.clicked.connect(self.start_animation)

    def start_animation(self):
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
