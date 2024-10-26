import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QGroupBox,
    QSpinBox,
    QComboBox,
    QTextEdit,
    QCheckBox,
    QRadioButton,
    QFormLayout,
)
from PyQt5.QtCore import Qt


class ComplexLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("复杂布局示例")
        self.setGeometry(100, 100, 800, 600)

        # 创建主布局
        main_layout = QHBoxLayout()

        # 左侧垂直布局
        left_layout = self.create_left_layout()
        main_layout.addLayout(left_layout, 1)

        # 右侧垂直布局
        right_layout = self.create_right_layout()
        main_layout.addLayout(right_layout, 2)

        # 设置主布局
        self.setLayout(main_layout)

    def create_left_layout(self):
        left_layout = QVBoxLayout()

        # 添加表单组
        form_group = self.create_form_layout()
        left_layout.addWidget(form_group)

        # 添加可伸缩空间
        left_layout.addStretch(1)

        # 添加选项组
        options_group = self.create_options_layout()
        left_layout.addWidget(options_group)

        return left_layout

    def create_right_layout(self):
        right_layout = QVBoxLayout()

        # 文本编辑区
        text_edit = QTextEdit()
        right_layout.addWidget(text_edit, 1)

        # 另一个文本编辑区
        text_edit2 = QTextEdit()
        right_layout.addWidget(text_edit2, 2)

        # 添加可伸缩空间
        right_layout.addStretch(1)

        # 按钮组
        button_layout = self.create_button_layout()
        right_layout.addLayout(button_layout)

        # 状态组
        status_group = self.create_status_layout()
        right_layout.addWidget(status_group)

        return right_layout

    def create_form_layout(self):
        form_group = QGroupBox("表单布局")
        form_layout = QFormLayout()
        
        form_layout.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)
        form_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        form_layout.setSpacing(10)
        form_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        form_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        
        form_layout.addRow("姓名:", QLineEdit())
        form_layout.addRow("年龄:", QSpinBox())
        form_layout.addRow("职业:", QComboBox())
        form_layout.addRow(QLabel("个人简介:"))
        form_layout.addRow(QTextEdit())
        
        hobby_label = QLabel("爱好:")
        hobby_layout = QHBoxLayout()
        hobby_layout.addWidget(QCheckBox("阅读"))
        hobby_layout.addWidget(QCheckBox("运动"))
        hobby_layout.addWidget(QCheckBox("音乐"))
        form_layout.addRow(hobby_label, hobby_layout)
        
        form_layout.addRow("电子邮件:", QLineEdit())
        
        form_group.setLayout(form_layout)
        return form_group

    def create_options_layout(self):
        options_group = QGroupBox("选项")
        options_layout = QVBoxLayout()
        options_layout.addWidget(QCheckBox("选项 1"))
        options_layout.addWidget(QCheckBox("选项 2"))
        options_layout.addWidget(QCheckBox("选项 3"))
        options_group.setLayout(options_layout)
        return options_group

    def create_button_layout(self):
        button_layout = QHBoxLayout()
        button_layout.addWidget(QPushButton("保存"))
        button_layout.addWidget(QPushButton("取消"))
        button_layout.addStretch(1)
        button_layout.addWidget(QPushButton("帮助"))
        return button_layout

    def create_status_layout(self):
        status_group = QGroupBox("状态")
        status_layout = QHBoxLayout()
        status_layout.addWidget(QRadioButton("正常"))
        status_layout.addWidget(QRadioButton("警告"))
        status_layout.addWidget(QRadioButton("错误"))
        status_group.setLayout(status_layout)
        return status_group

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ComplexLayoutDemo()
    demo.show()
    sys.exit(app.exec_())
