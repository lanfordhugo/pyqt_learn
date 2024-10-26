import sys, os
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import QThread, pyqtSignal

"""
高级数据库功能示例

知识点：
- 使用QSqlDatabase管理数据库连接。
- 使用QSqlTableModel和QSqlQueryModel来管理数据库表数据。
- 使用QThread在后台线程中执行数据库操作。
"""

class DatabaseThread(QThread):
    data_loaded = pyqtSignal()

    def run(self):
        """
        在后台线程中加载数据
        """
        db = QSqlDatabase.addDatabase('QSQLITE')
        db_path = os.path.join(os.path.dirname(__file__), 'advanced_db.db')
        db.setDatabaseName(db_path)
        if db.open():
            query = QSqlQuery()
            query.exec_("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customer_name TEXT, amount REAL)")
            query.exec_("INSERT INTO orders (customer_name, amount) VALUES ('Eve', 200.0)")
            query.exec_("INSERT INTO orders (customer_name, amount) VALUES ('Frank', 250.0)")
            db.close()
        self.data_loaded.emit()

def create_connection():
    """
    创建并打开数据库连接
    """
    db = QSqlDatabase.addDatabase('QSQLITE')
    db_path = os.path.join(os.path.dirname(__file__), 'advanced_db.db')
    db.setDatabaseName(db_path)

    if not db.open():
        print("无法连接到数据库")
        return False
    return True

def setup_model():
    """
    设置QSqlTableModel以管理数据库表
    """
    model = QSqlTableModel()
    model.setTable('orders')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    return model

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("高级订单管理")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        self.view = QTableView()
        self.model = setup_model()
        self.view.setModel(self.model)
        layout.addWidget(self.view)

        self.load_button = QPushButton("加载数据")
        self.load_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_button)

    def load_data(self):
        """
        使用后台线程加载数据
        """
        self.thread = DatabaseThread()
        self.thread.data_loaded.connect(self.on_data_loaded)
        self.thread.start()

    def on_data_loaded(self):
        """
        数据加载完成后刷新视图
        """
        self.model.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if create_connection():
        window = MainWindow()
        window.show()

    sys.exit(app.exec_())

