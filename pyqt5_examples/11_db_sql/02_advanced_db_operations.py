import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

"""
高级数据库操作示例

知识点：
- 事务管理：使用`QSqlDatabase.transaction()`来管理事务。
- 参数化查询：使用`QSqlQuery.prepare()`和`QSqlQuery.addBindValue()`来防止SQL注入。
"""

def create_connection():
    """
    创建并打开数据库连接
    """
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('advanced_db.db')

    if not db.open():
        print(f"无法连接到数据库: {db.lastError().text()}")
        return False
    return True

def create_table():
    """
    创建一个复杂的表
    """
    query = QSqlQuery()
    query.exec_("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customer_name TEXT, amount REAL)")

def insert_order(customer_name, amount):
    """
    插入订单数据，使用参数化查询防止SQL注入
    """
    query = QSqlQuery()
    query.prepare("INSERT INTO orders (customer_name, amount) VALUES (?, ?)")
    query.addBindValue(customer_name)
    query.addBindValue(amount)
    query.exec_()

def query_orders():
    """
    查询并打印订单数据
    """
    query = QSqlQuery()
    query.exec_("SELECT * FROM orders WHERE amount > 50.0")
    while query.next():
        id = query.value(0)
        customer_name = query.value(1)
        amount = query.value(2)
        print(f"Order ID: {id}, Customer: {customer_name}, Amount: {amount}")

def transaction_example():
    """
    演示事务管理
    """
    db = QSqlDatabase.database()
    db.transaction()  # 开始事务

    try:
        insert_order('Charlie', 75.0)
        insert_order('David', 100.0)
        db.commit()  # 提交事务
        print("事务提交成功")
    except Exception as e:
        db.rollback()  # 回滚事务
        print(f"事务失败，已回滚: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if create_connection():
        create_table()
        transaction_example()  # 执行事务示例
        query_orders()  # 查询订单数据

    sys.exit(app.exec_())

