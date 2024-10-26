import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QStatusBar, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('主窗口示例')
        self.setGeometry(100, 100, 400, 300)

        # 创建中央窗口部件
        central_widget = QLabel("这是中央窗口区域", self)
        self.setCentralWidget(central_widget)

        # 创建菜单栏
        menubar = self.menuBar()
        file_menu = menubar.addMenu('文件')
        
        # 添加菜单项
        exit_action = QAction('退出', self)
        exit_action.setStatusTip('退出应用程序')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # 创建状态栏
        self.statusBar().showMessage('准备就绪')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

