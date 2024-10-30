import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsLineItem, QMainWindow
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QBrush, QColor, QPen, QPainter  # 确保导入QPainter

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("图形视图框架扩展示例")
        
        # 创建场景
        self.scene = QGraphicsScene(self)
        
        # 添加椭圆
        ellipse = QGraphicsEllipseItem(0, 0, 100, 50)
        ellipse.setBrush(QBrush(QColor(255, 0, 0)))
        ellipse.setFlag(QGraphicsEllipseItem.ItemIsMovable)  # 允许拖动
        self.scene.addItem(ellipse)
        
        # 添加矩形
        rect = QGraphicsRectItem(150, 0, 100, 50)
        rect.setBrush(QBrush(QColor(0, 255, 0)))
        rect.setFlag(QGraphicsRectItem.ItemIsMovable)  # 允许拖动
        self.scene.addItem(rect)
        
        # 添加线条
        line = QGraphicsLineItem(0, 0, 250, 100)
        line.setPen(QPen(QColor(0, 0, 255), 2))
        self.scene.addItem(line)
        
        # 添加更多图形项
        for i in range(5):
            ellipse = QGraphicsEllipseItem(i * 30, i * 30, 20, 20)
            ellipse.setBrush(QBrush(QColor(255, 255, 0)))
            ellipse.setFlag(QGraphicsEllipseItem.ItemIsMovable)
            self.scene.addItem(ellipse)
        
        # 创建视图
        self.view = QGraphicsView(self.scene, self)
        self.view.setRenderHint(QPainter.Antialiasing)  # 使用QPainter.Antialiasing
        self.view.setDragMode(QGraphicsView.RubberBandDrag)  # 允许框选
        self.setCentralWidget(self.view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # 窗口大小
    window.resize(400, 300)

    window.show()
    sys.exit(app.exec_())
