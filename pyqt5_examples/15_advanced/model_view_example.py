import sys
from PyQt5.QtWidgets import QApplication, QTableView, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Model/View 编程示例")

        # 创建模型
        self.model = QStandardItemModel(4, 2)  # 4行2列
        self.model.setHorizontalHeaderLabels(["姓名", "年龄"])

        # 填充数据
        data = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 28)]

        for row, (name, age) in enumerate(data):
            self.model.setItem(row, 0, QStandardItem(name))
            self.model.setItem(row, 1, QStandardItem(str(age)))

        # 创建视图
        self.view = QTableView()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
