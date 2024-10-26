import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont

class ApplicationInfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QApplication 示例')
        
        layout = QVBoxLayout()

        # 使用QApplication.applicationName()获取应用程序名称
        app_name_label = QLabel(f"应用程序名称: {QApplication.applicationName()}")
        layout.addWidget(app_name_label)

        # 使用QApplication.applicationVersion()获取应用程序版本
        app_version_label = QLabel(f"应用程序版本: {QApplication.applicationVersion()}")
        layout.addWidget(app_version_label)

        # 使用QApplication.desktop()获取桌面信息，如屏幕大小
        desktop_info = QLabel(f"主屏幕大小: {QApplication.desktop().screenGeometry().width()}x{QApplication.desktop().screenGeometry().height()}")
        layout.addWidget(desktop_info)

        # 使用QApplication.font()获取应用程序的字体
        system_font = QApplication.font().family()
        font_info = QLabel(f"系统字体: {system_font}")
        layout.addWidget(font_info)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    # 创建QApplication实例，这是PyQt5应用程序的基础
    app = QApplication(sys.argv)
    
    # 使用setApplicationName()设置应用程序名称
    app.setApplicationName("QApplication 演示")
    # 使用setApplicationVersion()设置应用程序版本
    app.setApplicationVersion("1.0")

    # 使用setFont()设置应用程序范围的字体
    app.setFont(QFont("Arial", 12))

    # 创建并显示主窗口
    window = ApplicationInfoWindow()
    window.show()
    
    # 启动应用程序的事件循环
    sys.exit(app.exec_())
