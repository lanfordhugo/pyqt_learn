import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QMouseEvent


class MouseEventDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)  # 启用鼠标跟踪
        self.mouse_x, self.mouse_y = None, None  # 初始化鼠标坐标

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)  # 修改这行，添加高度参数
        self.setWindowTitle("鼠标事件演示")  # 设置窗口标题

        layout = QVBoxLayout()  # 创建垂直布局
        self.label = QLabel("鼠标事件将显示在这里")  # 创建标签用于显示鼠标事件信息
        layout.addWidget(self.label)  # 将标签添加到布局中
        self.setLayout(layout)  # 设置窗口的布局

        # 确保布局中的所有小部件也启用鼠标跟踪
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().setMouseTracking(True)

        self.show()  # 显示窗口

    def mousePressEvent(self, event):
        # 当鼠标按钮被按下时触发
        self.updateLabel("鼠标按下", event)

    def mouseReleaseEvent(self, event):
        # 当鼠标按钮被释放时触发
        self.updateLabel("鼠标释放", event)

    def mouseDoubleClickEvent(self, event):
        # 当鼠标双击时触发
        self.updateLabel("鼠标双击", event)

    def mouseMoveEvent(self, event: QMouseEvent):
        # 当鼠标移动时触发
        self.mouse_x, self.mouse_y = event.x(), event.y()  # 更新鼠标坐标
        self.updateLabel("鼠标移动", event)
        print(f"鼠标移动 - 位置: ({self.mouse_x}, {self.mouse_y})")
        self.update()  # 触发重绘事件，以更新小红点的位置

    def enterEvent(self, event):
        # 当鼠标进入窗口时触发
        self.label.setText("鼠标进入窗口")

    def leaveEvent(self, event):
        # 当鼠标离开窗口时触发
        self.label.setText("鼠标离开窗口")
        self.mouse_x, self.mouse_y = None, None  # 清除鼠标坐标
        self.update()  # 触发重绘事件，以移除小红点

    def wheelEvent(self, event):
        # 当鼠标滚轮滚动时触发
        delta = event.angleDelta().y()
        if delta > 0:
            self.label.setText("鼠标滚轮向上滚动")
        else:
            self.label.setText("鼠标滚轮向下滚动")

    def updateLabel(self, action, event):
        # 更新标签文本以显示鼠标事件信息
        button = {
            Qt.LeftButton: "左键",
            Qt.RightButton: "右键",
            Qt.MiddleButton: "中键",
            Qt.NoButton: "无按键",  # 添加这一行以处理无按键的情况
        }.get(event.button(), "未知按键")

        self.label.setText(f"{action}: {button} 在 ({event.x()}, {event.y()})")

    def paintEvent(self, event):
        super().paintEvent(event)  # 调用父类的paintEvent以确保正确的绘制行为
        if self.mouse_x is not None and self.mouse_y is not None:
            painter = QPainter(self)
            painter.setPen(QColor(255, 0, 0))
            painter.setBrush(QColor(255, 0, 0))  # 设置画刷颜色，使圆点填充
            painter.drawEllipse(self.mouse_x - 5, self.mouse_y - 5, 10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建QApplication实例
    ex = MouseEventDemo()  # 创建MouseEventDemo实例
    sys.exit(app.exec_())  # 进入应用程序的主循环
