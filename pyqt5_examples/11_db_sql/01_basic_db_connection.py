import os
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

"""
基本数据库连接示例

知识点：
- 使用QSqlDatabase管理数据库连接。
- 使用QSqlQuery执行SQL查询。
"""

def create_connection():
    """
    创建并打开数据库连接
    """
    db_path = os.path.join(os.path.dirname(__file__), 'basic_db.db')
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_path)

    if not db.open():
        print(f"无法连接到数据库: {db.lastError().text()}")
        return False
    return True

def create_table():
    """
    创建一个简单的表
    """
    query = QSqlQuery()
    query.exec_("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT)")

def insert_data():
    """
    插入示例数据
    """
    query = QSqlQuery()
    query.exec_("INSERT INTO people (name) VALUES ('Alice')")
    query.exec_("INSERT INTO people (name) VALUES ('Bob')")

def query_data():
    """
    查询并打印表中的数据
    """
    query = QSqlQuery()
    query.exec_("SELECT * FROM people")
    while query.next():
        id = query.value(0)
        name = query.value(1)
        print(f"ID: {id}, Name: {name}")

def close_connection():
    """
    关闭数据库连接
    """
    db = QSqlDatabase.database()
    db.close()
    QSqlDatabase.removeDatabase('')  # 使用空字符串来移除默认连接

if __name__ == '__main__':
    if create_connection():
        create_table()
        insert_data()
        query_data()
        close_connection()  # 关闭数据库连接
