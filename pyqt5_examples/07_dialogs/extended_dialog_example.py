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
    QGridLayout,
)
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt
import sys


class ExtendedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("扩展对话框示例")

        layout = QGridLayout()

        buttons = [
            ("信息消息框", self.showInfoMessage),
            ("警告消息框", self.showWarningMessage),
            ("错误消息框", self.showCriticalMessage),
            ("问题消息框", self.showQuestionMessage),
            ("自定义消息框", self.showCustomMessage),
            ("输入对话框", self.showInputDialog),
            ("文件对话框", self.showFileDialog),
            ("颜色对话框", self.showColorDialog),
            ("字体对话框", self.showFontDialog),
        ]

        positions = [(i, j) for i in range(3) for j in range(3)]

        for position, (name, func) in zip(positions, buttons):
            button = QPushButton(name)
            button.clicked.connect(func)
            layout.addWidget(button, *position)

        self.setLayout(layout)
        self.show()

    def showInfoMessage(self):
        reply = QMessageBox.information(
            self, "信息", "这是一个信息消息框", QMessageBox.Ok | QMessageBox.Cancel
        )
        self.printReply("信息消息框", reply)

    def showWarningMessage(self):
        reply = QMessageBox.warning(
            self, "警告", "这是一个警告消息框", QMessageBox.Ok | QMessageBox.Cancel
        )
        self.printReply("警告消息框", reply)

    def showCriticalMessage(self):
        reply = QMessageBox.critical(
            self, "错误", "这是一个错误消息框", QMessageBox.Ok | QMessageBox.Cancel
        )
        self.printReply("错误消息框", reply)

    def showQuestionMessage(self):
        reply = QMessageBox.question(
            self,
            "问题",
            "这是一个问题消息框",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        )
        self.printReply("问题消息框", reply)

    def showCustomMessage(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("这是一个自定义消息框")
        msgBox.setWindowTitle("自定义")
        msgBox.setStandardButtons(
            QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Apply
        )
        msgBox.setDefaultButton(QMessageBox.Ok)
        reply = msgBox.exec_()
        self.printReply("自定义消息框", reply)

    def showInputDialog(self):
        text, ok = QInputDialog.getText(
            self, "输入对话框", "请输入您的名字：", QLineEdit.Normal, ""
        )
        if ok and text:
            print(f"输入对话框：用户输入了 '{text}'")
        else:
            print("输入对话框：用户取消了输入")

    def showFileDialog(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "所有文件 (*);;文本文件 (*.txt)"
        )
        if fname:
            print(f"文件对话框：用户选择了文件 '{fname}'")
        else:
            print("文件对话框：用户取消了选择")

    def showColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")
            print(f"颜色对话框：用户选择了颜色 {color.name()}")
        else:
            print("颜色对话框：用户取消了选择")

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.setFont(font)
            print(f"字体对话框：用户选择了字体 {font.family()}, {font.pointSize()}pt")
        else:
            print("字体对话框：用户取消了选择")

    def printReply(self, dialog_type, reply):
        if reply == QMessageBox.Ok:
            print(f"{dialog_type}：用户点击了 Ok")
        elif reply == QMessageBox.Cancel:
            print(f"{dialog_type}：用户点击了 Cancel")
        elif reply == QMessageBox.Yes:
            print(f"{dialog_type}：用户点击了 Yes")
        elif reply == QMessageBox.No:
            print(f"{dialog_type}：用户点击了 No")
        elif reply == QMessageBox.Apply:
            print(f"{dialog_type}：用户点击了 Apply")
        else:
            print(f"{dialog_type}：用户关闭了对话框")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ExtendedExample()
    sys.exit(app.exec_())
