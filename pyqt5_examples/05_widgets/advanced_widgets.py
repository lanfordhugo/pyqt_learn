import sys
from typing import Any
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
                             QListWidget, QTableWidget, QTreeWidget, QTabWidget, QDateTimeEdit,
                             QScrollArea, QTableWidgetItem, QTreeWidgetItem, QDateEdit, QTimeEdit,
                             QListWidgetItem, QInputDialog, QLineEdit, QCheckBox)
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime
from PyQt5.QtGui import QIcon

class AdvancedWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle('PyQt5高级控件示例')
        self.setGeometry(100, 100, 800, 800)

        # 创建一个滚动区域
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scroll)

        # 创建一个容器widget
        container = QWidget()
        scroll.setWidget(container)

        layout = QVBoxLayout(container)

        # 添加高级控件
        self.add_advanced_widgets(layout)

    def add_advanced_widgets(self, layout: QVBoxLayout) -> None:
        # 日期编辑器 (QDateEdit)
        layout.addWidget(QLabel('<b>日期编辑器 (QDateEdit)</b>'))
        date_edit = QDateEdit(self)
        date_edit.setDate(QDateTime.currentDateTime().date())
        date_edit.setCalendarPopup(True)
        layout.addWidget(date_edit)

        # 时间编辑器 (QTimeEdit)
        layout.addWidget(QLabel('<b>时间编辑器 (QTimeEdit)</b>'))
        time_edit = QTimeEdit(self)
        time_edit.setTime(QDateTime.currentDateTime().time())
        layout.addWidget(time_edit)

        # 添加一个标签来显示选择的日期和时间
        self.date_time_label = QLabel("当前选择: " + QDateTime(date_edit.date(), time_edit.time()).toString("yyyy-MM-dd HH:mm:ss"))
        layout.addWidget(self.date_time_label)

        layout.addSpacing(10)

        # 列表控件 (QListWidget)
        layout.addWidget(QLabel('<b>列表控件 (QListWidget)</b>'))
        list_layout = QVBoxLayout()
        self.list_widget = QListWidget(self)
        self.list_widget.addItems(['项目1', '项目2', '项目3'])
        self.list_widget.itemClicked.connect(self.on_item_clicked)

        list_layout.addWidget(self.list_widget)

        # 添加控制按钮
        button_layout = QHBoxLayout()
        add_item_btn = QPushButton('添加项目')
        add_item_btn.clicked.connect(self.add_list_item)
        remove_item_btn = QPushButton('删除选中项')
        remove_item_btn.clicked.connect(self.remove_list_item)
        clear_list_btn = QPushButton('清空列表')
        clear_list_btn.clicked.connect(self.clear_list)

        button_layout.addWidget(add_item_btn)
        button_layout.addWidget(remove_item_btn)
        button_layout.addWidget(clear_list_btn)

        list_layout.addLayout(button_layout)

        # 添加显示选中项的标签
        self.selected_item_label = QLabel('当前选中: 无')
        list_layout.addWidget(self.selected_item_label)

        layout.addLayout(list_layout)

        layout.addSpacing(10)

        # 表格控件 (QTableWidget)
        layout.addWidget(QLabel('<b>表格控件 (QTableWidget)</b>'))
        table_layout = QVBoxLayout()
        self.table = QTableWidget(5, 5, self)
        self.table.setMinimumHeight(200)
        self.table.setHorizontalHeaderLabels(['列1', '列2', '列3', '列4', '列5'])

        # 初始化表格内容
        for i in range(5):
            for j in range(5):
                self.table.setItem(i, j, QTableWidgetItem(f'单元格 {i},{j}'))

        table_layout.addWidget(self.table)

        # 添加按钮来控制行和列
        button_layout = QHBoxLayout()
        add_row_btn = QPushButton('添加行')
        add_row_btn.clicked.connect(self.add_row)
        del_row_btn = QPushButton('删除行')
        del_row_btn.clicked.connect(self.del_row)
        add_col_btn = QPushButton('添加列')
        add_col_btn.clicked.connect(self.add_column)
        del_col_btn = QPushButton('删除列')
        del_col_btn.clicked.connect(self.del_column)

        button_layout.addWidget(add_row_btn)
        button_layout.addWidget(del_row_btn)
        button_layout.addWidget(add_col_btn)
        button_layout.addWidget(del_col_btn)

        table_layout.addLayout(button_layout)
        layout.addLayout(table_layout)

        layout.addSpacing(10)

        # 树形控件 (QTreeWidget)
        layout.addWidget(QLabel('<b>树形控件 (QTreeWidget)</b>'))
        self.tree = QTreeWidget(self)
        self.tree.setHeaderLabels(['名称', '描述'])
        self.tree.setColumnWidth(0, 150)

        # 添加顶级项目
        root = QTreeWidgetItem(self.tree, ['项目'])
        root.setIcon(0, QIcon('folder.png'))  # 确保你有一个folder.png文件，或使用其他图标

        # 添加子项目
        child1 = QTreeWidgetItem(root, ['子项目1', '这是子项目1的描述'])
        child2 = QTreeWidgetItem(root, ['子项目2', '这是子项目2的描述'])
        child1.setIcon(0, QIcon('file.png'))  # 确保你有一个file.png文件，或使用其他图标
        child2.setIcon(0, QIcon('file.png'))

        # 添加孙项目
        grandchild = QTreeWidgetItem(child1, ['孙项目', '这是孙项目的描述'])
        grandchild.setIcon(0, QIcon('file.png'))

        self.tree.expandAll()  # 展开所有项目
        self.tree.itemClicked.connect(self.onTreeItemClicked)

        layout.addWidget(self.tree)

        # 添加用于显示选中项的标签
        self.tree_label = QLabel('当前选中: 无')
        layout.addWidget(self.tree_label)

        layout.addSpacing(10)

        # 标签页控件 (QTabWidget)
        layout.addWidget(QLabel('<b>标签页控件 (QTabWidget)</b>'))
        self.tab_widget = QTabWidget(self)

        # 创建并添加第一个标签页
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(QLabel('这是第一个标签页的内容'))
        tab1_layout.addWidget(QPushButton('标签页1按钮'))
        self.tab_widget.addTab(tab1, '标签1')

        # 创建并添加第二个标签页
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(QLabel('这是第二个标签页的内容'))
        tab2_layout.addWidget(QLineEdit('可编辑文本'))
        self.tab_widget.addTab(tab2, '标签2')

        # 创建并添加第三个标签页
        tab3 = QWidget()
        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(QLabel('这是第三个标签页的内容'))
        tab3_layout.addWidget(QCheckBox('复选框'))
        self.tab_widget.addTab(tab3, '标签3')

        self.tab_widget.currentChanged.connect(self.onTabChanged)

        layout.addWidget(self.tab_widget)

        # 添加用于显示当前标签页的标签
        self.tab_label = QLabel('当前标签页: 标签1')
        layout.addWidget(self.tab_label)

        layout.addSpacing(10)

    def update_date_time_label(self, qdate: QDate, qtime: QTime) -> None:
        self.date_time_label.setText("当前选择: " + QDateTime(qdate, qtime).toString("yyyy-MM-dd HH:mm:ss"))

    def add_row(self) -> None:
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        for i in range(self.table.columnCount()):
            self.table.setItem(row_count, i, QTableWidgetItem(f'新单元格 {row_count},{i}'))

    def del_row(self) -> None:
        if self.table.rowCount() > 0:
            self.table.removeRow(self.table.rowCount() - 1)

    def add_column(self) -> None:
        col_count = self.table.columnCount()
        self.table.insertColumn(col_count)
        self.table.setHorizontalHeaderItem(col_count, QTableWidgetItem(f'新列{col_count+1}'))
        for i in range(self.table.rowCount()):
            self.table.setItem(i, col_count, QTableWidgetItem(f'新单元格 {i},{col_count}'))

    def del_column(self) -> None:
        if self.table.columnCount() > 0:
            self.table.removeColumn(self.table.columnCount() - 1)

    def add_list_item(self) -> None:
        text, ok = QInputDialog.getText(self, '添加项目', '请输入新项目:')
        if ok and text:
            self.list_widget.addItem(text)

    def remove_list_item(self) -> None:
        current_item = self.list_widget.currentItem()
        if current_item:
            row = self.list_widget.row(current_item)
            self.list_widget.takeItem(row)
            self.selected_item_label.setText('当前选中: 无')

    def clear_list(self) -> None:
        self.list_widget.clear()
        self.selected_item_label.setText('当前选中: 无')

    def on_item_clicked(self, item: QListWidgetItem) -> None:
        self.selected_item_label.setText(f'当前选中: {item.text()}')

    def onTreeItemClicked(self, item, column):
        """
        处理树形控件项目被点击的事件。
        
        :param item: 被点击的树形项目
        :param column: 被点击的列
        """
        self.tree_label.setText(f'当前选中: {item.text(0)} - {item.text(1)}')

    def onTabChanged(self, index):
        """
        处理标签页切换的事件。
        
        :param index: 新的当前标签页的索引
        """
        self.tab_label.setText(f'当前标签页: {self.tab_widget.tabText(index)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdvancedWidgets()
    ex.show()
    sys.exit(app.exec_())
