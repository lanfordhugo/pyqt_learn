import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class WidgetDragDropDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('控件拖放示例')  # 设置窗口标题
        self.setGeometry(100, 100, 400, 400)  # 设置窗口位置和大小

        central_widget = QWidget()  # 创建中央小部件
        self.setCentralWidget(central_widget)  # 设置中央小部件
        layout = QGridLayout(central_widget)  # 创建网格布局

        self.reorderable_grid = ReorderableGrid()  # 创建可重排网格
        layout.addWidget(self.reorderable_grid)  # 将可重排网格添加到布局中

class DraggableLabel(QLabel):
    def __init__(self, color, text):
        super().__init__()
        self.setText(text)  # 设置标签文本
        self.setAlignment(Qt.AlignCenter)  # 设置文本居中对齐
        self.setStyleSheet(f"""
            background-color: {color};
            border: 1px solid black;
            min-width: 100px;
            min-height: 100px;
        """)  # 设置标签样式

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # 检查是否按下左键
            self.drag_start_position = event.pos()  # 记录拖动起始位置

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):  # 检查是否按住左键
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return  # 检查拖动距离是否超过最小拖动距离

        drag = QDrag(self)  # 创建拖动对象
        mime_data = QMimeData()  # 创建MIME数据对象
        mime_data.setText(self.text())  # 设置MIME数据文本
        drag.setMimeData(mime_data)  # 将MIME数据设置到拖动对象中

        drag.exec_(Qt.MoveAction)  # 执行拖动操作

class ReorderableGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.initGrid()  # 初始化网格

    def initGrid(self):
        layout = QGridLayout(self)  # 创建网格布局
        colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'gray', 'orange', 'purple']  # 定义颜色列表
        for i in range(3):
            for j in range(3):
                label = DraggableLabel(colors[i*3 + j], f"项目 {i*3 + j + 1}")  # 创建可拖动标签
                layout.addWidget(label, i, j)  # 将标签添加到网格布局中

        self.setAcceptDrops(True)  # 设置接受拖放

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():  # 检查MIME数据是否包含文本
            event.accept()  # 接受拖动事件
        else:
            event.ignore()  # 忽略拖动事件

    def dropEvent(self, event):
        pos = event.pos()  # 获取拖放位置
        widget = self.childAt(pos)  # 获取拖放位置的子控件
        if widget:
            source = event.source()  # 获取拖动源控件
            layout = self.layout()  # 获取网格布局
            source_index = layout.indexOf(source)  # 获取拖动源控件的索引
            target_index = layout.indexOf(widget)  # 获取目标控件的索引
            
            if source_index != -1 and target_index != -1:
                source_row, source_col, _, _ = layout.getItemPosition(source_index)  # 获取拖动源控件的位置
                target_row, target_col, _, _ = layout.getItemPosition(target_index)  # 获取目标控件的位置
                
                layout.removeWidget(source)  # 从布局中移除拖动源控件
                layout.removeWidget(widget)  # 从布局中移除目标控件
                
                layout.addWidget(source, target_row, target_col)  # 将拖动源控件添加到目标位置
                layout.addWidget(widget, source_row, source_col)  # 将目标控件添加到拖动源位置

        event.accept()  # 接受拖放事件

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = WidgetDragDropDemo()
    demo.show()
    sys.exit(app.exec_())
