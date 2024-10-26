import sys
from typing import Any
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, 
                             QTextEdit, QCheckBox, QRadioButton, QComboBox, QSlider, 
                             QProgressBar, QVBoxLayout, QHBoxLayout, QGroupBox, 
                             QSpinBox)
from PyQt5.QtCore import Qt, QTimer

class CommonWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowTitle('PyQt5常用控件示例')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # 原有的基础控件
        self.add_simple_widgets(layout)

        self.setLayout(layout)

    def add_simple_widgets(self, layout: QVBoxLayout) -> None:
        # 标签 (QLabel)
        layout.addWidget(QLabel('<b>标签 (QLabel)</b>'))
        label = QLabel('这是一个标签', self)
        layout.addWidget(label)
        
        layout.addSpacing(10)

        # 按钮 (QPushButton) 和点击次数标签
        layout.addWidget(QLabel('<b>按钮 (QPushButton) 和点击次数</b>'))
        button = QPushButton('点击我', self)
        self.click_count_label = QLabel('点击次数: 0', self)
        self.click_count = 0
        button.clicked.connect(self.buttonClicked)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button)
        button_layout.addWidget(self.click_count_label)
        layout.addLayout(button_layout)

        layout.addSpacing(10)

        # 单行文本框 (QLineEdit)
        layout.addWidget(QLabel('<b>单行文本框 (QLineEdit)</b>'))
        self.lineEdit = QLineEdit(self)
        layout.addWidget(self.lineEdit)

        layout.addSpacing(10)

        # 多行文本框 (QTextEdit)
        layout.addWidget(QLabel('<b>多行文本框 (QTextEdit)</b>'))
        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        layout.addSpacing(10)

        # 复选框 (QCheckBox)
        layout.addWidget(QLabel('<b>复选框 (QCheckBox)</b>'))
        checkbox_layout = QHBoxLayout()
        checkbox1 = QCheckBox('选项1', self)
        checkbox2 = QCheckBox('选项2', self)
        checkbox_layout.addWidget(checkbox1)
        checkbox_layout.addWidget(checkbox2)
        layout.addLayout(checkbox_layout)

        layout.addSpacing(10)

        # 单选按钮 (QRadioButton)
        layout.addWidget(QLabel('<b>单选按钮 (QRadioButton)</b>'))
        radioGroup = QGroupBox()
        radioLayout = QHBoxLayout()
        radio1 = QRadioButton('选项1')
        radio2 = QRadioButton('选项2')
        radioLayout.addWidget(radio1)
        radioLayout.addWidget(radio2)
        radioGroup.setLayout(radioLayout)
        layout.addWidget(radioGroup)

        layout.addSpacing(10)

        # 下拉列表 (QComboBox)
        layout.addWidget(QLabel('<b>下拉列表 (QComboBox)</b>'))
        combo = QComboBox(self)
        combo.addItems(['选项1', '选项2', '选项3'])
        layout.addWidget(combo)

        layout.addSpacing(10)

        # 数字输入框 (QSpinBox)
        layout.addWidget(QLabel('<b>数字输入框 (QSpinBox)</b>'))
        spinbox = QSpinBox(self)
        layout.addWidget(spinbox)

        layout.addSpacing(10)

        # 滑块 (QSlider)
        layout.addWidget(QLabel('<b>滑块 (QSlider)</b>'))
        slider_layout = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.updateSliderLabel)
        self.slider_label = QLabel('50%', self)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_label)
        layout.addLayout(slider_layout)

        layout.addSpacing(10)

        # 进度条 (QProgressBar)
        layout.addWidget(QLabel('<b>进度条 (QProgressBar)</b>'))
        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(0)
        layout.addWidget(self.progressBar)
        
        # 创建定时器，每100毫秒更新一次进度条
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgressBar)
        self.timer.start(100)

    # 按钮点击事件
    def buttonClicked(self) -> None:
        self.click_count += 1
        self.click_count_label.setText(f'点击次数: {self.click_count}')
            
    # 更新滑块标签
    def updateSliderLabel(self) -> None:
        self.slider_label.setText(f'{self.slider.value()}%')
        
    # 进度条
    def updateProgressBar(self) -> None:
        self.progressBar.setValue(self.progressBar.value() + 1)
        if self.progressBar.value() == 100:
            self.progressBar.setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CommonWidgets()
    ex.show()
    sys.exit(app.exec_())
