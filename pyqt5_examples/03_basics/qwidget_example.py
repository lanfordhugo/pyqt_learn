
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QColor
import random

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('我的第一个QWidget')
        self.setGeometry(300, 300, 300, 200)

        # 创建一个按钮
        btn = QPushButton('点击我', self)
        btn.clicked.connect(self.changeColor)

        # 创建垂直布局并添加按钮
        layout = QVBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)

    def changeColor(self):
        # 随机改变背景颜色
        color = QColor.fromHsv(random.randint(0, 359), 255, 255)
        self.setStyleSheet(f"background-color: {color.name()};")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())