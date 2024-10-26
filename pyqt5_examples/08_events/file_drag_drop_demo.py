import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class FileDragDropDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle('文件拖放示例')  # 设置窗口标题
        self.setGeometry(100, 100, 300, 200)  # 设置窗口位置和大小

        central_widget = QWidget()  # 创建中央小部件
        self.setCentralWidget(central_widget)  # 设置中央小部件
        layout = QVBoxLayout(central_widget)  # 创建垂直布局并设置为中央小部件的布局

        self.file_drop_area = FileDropArea()  # 创建文件拖放区域
        layout.addWidget(self.file_drop_area)  # 将文件拖放区域添加到布局中

class FileDropArea(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("将文件拖到这里")  # 设置标签文本
        self.setAlignment(Qt.AlignCenter)  # 设置文本居中对齐
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;  # 设置标签的边框样式
                border-radius: 5px;  # 设置标签的圆角半径
                background-color: #f0f0f0;  # 设置标签的背景颜色
                min-width: 200px;  # 设置标签的最小宽度
                min-height: 200px;  # 设置标签的最小高度
            }
        """)
        self.setAcceptDrops(True)  # 启用拖放功能

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():  # 如果拖入的数据包含URL
            event.accept()  # 接受拖放事件
        else:
            event.ignore()  # 忽略拖放事件

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]  # 获取拖入的文件路径
        self.setText(f"已接收文件:\n{', '.join(files)}")  # 更新标签文本显示接收的文件

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    demo = FileDragDropDemo()  # 创建主窗口对象
    demo.show()  # 显示主窗口
    sys.exit(app.exec_())  # 进入应用程序主循环
