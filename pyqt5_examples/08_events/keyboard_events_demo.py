import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QKeySequence

class KeyboardEventDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.key_hold_timer = QTimer()
        self.key_hold_timer.timeout.connect(self.onKeyHold)
        self.held_key = None

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("键盘事件演示")

        layout = QVBoxLayout()
        self.label = QLabel("键盘事件将显示在这里")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setFocus()  # 确保窗口获得焦点以接收键盘事件
        self.show()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return  # 忽略自动重复的按键事件
        key = event.key()
        key_name = QKeySequence(key).toString()
        self.updateLabel(f"按键按下: {key_name}")
        self.held_key = key
        self.key_hold_timer.start(1000)  # 1秒后触发长按事件

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return  # 忽略自动重复的按键事件
        key = event.key()
        key_name = QKeySequence(key).toString()
        self.updateLabel(f"按键释放: {key_name}")
        self.key_hold_timer.stop()
        self.held_key = None

    def onKeyHold(self):
        if self.held_key:
            key_name = QKeySequence(self.held_key).toString()
            self.updateLabel(f"按键长按: {key_name}")

    def updateLabel(self, text):
        self.label.setText(text)
        print(text)  # 同时在控制台打印事件信息

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = KeyboardEventDemo()
    sys.exit(app.exec_())
