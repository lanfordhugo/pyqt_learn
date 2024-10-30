import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class StyledWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建按钮
        self.button = QPushButton("点击我")

        # 设置样式表
        self.button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50; /* 绿色背景 */
                color: white; /* 白色文字 */
                border-radius: 10px; /* 圆角 */
                padding: 10px; /* 内边距 */
            }
            QPushButton:hover {
                background-color: #45a049; /* 鼠标悬停时的颜色 */
            }
        """
        )

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        # 窗口设置
        self.setWindowTitle("样式示例")
        self.resize(300, 200)


def main():
    app = QApplication(sys.argv)
    window = StyledWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
