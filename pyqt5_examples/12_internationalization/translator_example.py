import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建一个标签
        self.label = QLabel(self.tr("Hello, World!"))

        # 创建一个按钮用于切换语言
        self.switch_button = QPushButton(self.tr("Switch Language"))
        self.switch_button.clicked.connect(self.switch_language)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.switch_button)
        self.setLayout(layout)

        # 设置窗口标题
        self.setWindowTitle(self.tr("Internationalization Example"))

        # 初始化翻译器
        self.translator = QTranslator()
        self.current_locale = QLocale.system().name()
        self.qt_translations_path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)

    def switch_language(self):
        # 切换语言
        if self.current_locale.startswith("en"):
            self.current_locale = "zh_CN"  # 切换到中文
        else:
            self.current_locale = "en_US"  # 切换回英语

        # 加载新的翻译文件
        if self.translator.load("qt_" + self.current_locale, self.qt_translations_path):
            QApplication.instance().installTranslator(self.translator)

        # 更新界面文本
        self.label.setText(self.tr("Hello, World!"))
        self.switch_button.setText(self.tr("Switch Language"))
        self.setWindowTitle(self.tr("Internationalization Example"))

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
