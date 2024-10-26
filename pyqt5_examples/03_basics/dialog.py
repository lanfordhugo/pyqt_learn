import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLabel

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('自定义对话框')
        self.setGeometry(200, 200, 300, 100)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('这是一个自定义对话框'))
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对话框示例')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        btn = QPushButton('打开对话框', self)
        btn.clicked.connect(self.showDialog)
        layout.addWidget(btn)
        self.setLayout(layout)

    def showDialog(self):
        dialog = CustomDialog()
        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
