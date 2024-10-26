from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QInputDialog,
    QLineEdit,
    QFileDialog,
    QColorDialog,
    QFontDialog,
)
from PyQt5.QtGui import QColor, QFont
import sys


class ExtendedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle("扩展对话框示例")

        layout = QVBoxLayout()

        btn1 = QPushButton("信息消息框", self)
        btn1.clicked.connect(self.showInfoMessage)
        layout.addWidget(btn1)

        btn2 = QPushButton("警告消息框", self)
        btn2.clicked.connect(self.showWarningMessage)
        layout.addWidget(btn2)

        btn3 = QPushButton("错误消息框", self)
        btn3.clicked.connect(self.showCriticalMessage)
        layout.addWidget(btn3)

        btn4 = QPushButton("输入对话框", self)
        btn4.clicked.connect(self.showInputDialog)
        layout.addWidget(btn4)

        btn5 = QPushButton("文件对话框", self)
        btn5.clicked.connect(self.showFileDialog)
        layout.addWidget(btn5)

        btn6 = QPushButton("颜色对话框", self)
        btn6.clicked.connect(self.showColorDialog)
        layout.addWidget(btn6)

        btn7 = QPushButton("字体对话框", self)
        btn7.clicked.connect(self.showFontDialog)
        layout.addWidget(btn7)

        self.setLayout(layout)
        self.show()

    def showInfoMessage(self):
        QMessageBox.information(self, "信息", "这是一个信息消息框", QMessageBox.Yes)

    def showWarningMessage(self):
        QMessageBox.warning(self, "警告", "这是一个警告消息框", QMessageBox.Ok)

    def showCriticalMessage(self):
        QMessageBox.critical(self, "错误", "这是一个错误消息框", QMessageBox.Ok)

    def showInputDialog(self):
        text, ok = QInputDialog.getText(
            self, "输入对话框", "请输入您的名字：", QLineEdit.Normal, ""
        )
        if ok and text:
            QMessageBox.information(
                self, "输入结果", f"您输入的名字是：{text}", QMessageBox.Ok
            )

    def showFileDialog(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "所有文件 (*);;文本文件 (*.txt)"
        )
        if fname:
            QMessageBox.information(
                self, "文件选择", f"您选择的文件是：{fname}", QMessageBox.Ok
            )

    def showColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ExtendedExample()
    sys.exit(app.exec_())
