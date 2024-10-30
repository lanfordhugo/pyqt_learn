import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt

"""
简单绘图示例

总结：
1. 功能描述：
   - 展示PyQt5的基础绘图能力
   - 包含直线、矩形、圆形、文本等基本图形绘制
   - 演示如何设置画笔、画刷和颜色

"""

class DrawingDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 设置窗口基本属性
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('PyQt5绘图示例')
        
    def paintEvent(self, event):
        # 创建QPainter对象
        painter = QPainter()
        # 开始在窗口进行绘制
        painter.begin(self)
        
        # 设置画笔
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        painter.setPen(pen)
        
        # 绘制直线
        painter.drawLine(50, 50, 200, 50)
        
        # 设置画刷（用于填充）
        brush = QBrush(Qt.green, Qt.SolidPattern)
        painter.setBrush(brush)
        
        # 绘制矩形
        painter.drawRect(50, 80, 100, 60)
        
        # 绘制圆形
        painter.setBrush(QBrush(Qt.blue))
        painter.drawEllipse(50, 160, 100, 100)
        
        # 绘制文本
        painter.setPen(QPen(Qt.black))
        painter.drawText(200, 150, "Hello, PyQt5!")
        
        # 结束绘制
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DrawingDemo()
    demo.show()
    sys.exit(app.exec_())