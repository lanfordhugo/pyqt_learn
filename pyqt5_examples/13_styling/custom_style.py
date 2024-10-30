import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import QRect, Qt

class CustomButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumSize(100, 40)  # 设置按钮的最小尺寸

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(0, 0, self.width(), self.height())

        # 自定义绘制背景
        painter.setBrush(QColor(100, 150, 200))  # 设置背景颜色
        painter.setPen(Qt.NoPen)  # 去掉边框
        painter.drawRect(rect)

        # 自定义绘制文本
        painter.setPen(QColor(255, 255, 255))  # 设置文本颜色
        painter.setFont(QFont('Arial', 12))  # 设置字体
        # 使用正确的参数调用drawText
        painter.drawText(rect, Qt.AlignCenter, self.text())  # 居中绘制文本

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # 使用自定义按钮
        custom_button = CustomButton('Custom Button', self)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(custom_button)
        self.setLayout(layout)

        self.setWindowTitle('Custom Button Example')
        self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
