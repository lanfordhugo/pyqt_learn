import sys, os
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery

"""
模型视图集成示例

知识点：
- QSqlTableModel：用于管理数据库表数据。
- QTableView：用于显示数据库表数据。
- 使用QSqlQueryModel执行自定义查询。
"""

def create_connection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db_path = os.path.join(os.path.dirname(__file__), 'advanced_model_view_db.db')
    db.setDatabaseName(db_path)

    if not db.open():
        print("无法连接到数据库")
        return False

    query = QSqlQuery()
    query.exec_("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    
    query.exec_("SELECT COUNT(*) FROM products")
    if query.next() and query.value(0) == 0:
        query.exec_("INSERT INTO products (name, price) VALUES ('Laptop', 1200.0)")
        query.exec_("INSERT INTO products (name, price) VALUES ('Smartphone', 800.0)")

    return True

def setup_table_model():
    model = QSqlTableModel()
    model.setTable('products')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    return model

def setup_query_model():
    model = QSqlQueryModel()
    model.setQuery("SELECT name, price FROM products WHERE price > 1000")
    return model

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("产品管理")
        self.resize(800, 600)

        layout = QVBoxLayout(self)

        self.table_view = QTableView()
        self.table_model = setup_table_model()
        self.table_view.setModel(self.table_model)
        self.table_view.setSortingEnabled(True)
        layout.addWidget(self.table_view)

        query_label = QLabel("显示价格大于1000的产品")
        layout.addWidget(query_label)

        self.query_view = QTableView()
        self.query_model = setup_query_model()
        self.query_view.setModel(self.query_model)
        layout.addWidget(self.query_view)

        button_layout = QHBoxLayout()
        add_button = QPushButton("添加产品")
        add_button.clicked.connect(self.add_product)
        button_layout.addWidget(add_button)

        delete_button = QPushButton("删除选中产品")
        delete_button.clicked.connect(self.delete_selected_product)
        button_layout.addWidget(delete_button)

        layout.addLayout(button_layout)

        # 连接dataChanged信号到更新查询视图的槽
        self.table_model.dataChanged.connect(self.update_query_view)

    def add_product(self):
        row = self.table_model.rowCount()
        self.table_model.insertRow(row)
        self.table_model.setData(self.table_model.index(row, 1), "New Product")
        self.table_model.setData(self.table_model.index(row, 2), 0.0)
        self.table_model.submitAll()

    def delete_selected_product(self):
        selected = self.table_view.selectionModel().selectedRows()
        for index in selected:
            self.table_model.removeRow(index.row())
        self.table_model.submitAll()
        self.table_model.select()

    def update_query_view(self):
        self.query_view.setModel(setup_query_model())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if create_connection():
        window = MainWindow()
        window.show()

    sys.exit(app.exec_())
