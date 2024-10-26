import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSignal, pyqtSlot

"""
一个综合性的例子，展示PyQt5中信号与槽的多种用法。这个例子将包含一个简单的计算器界面，展示自定义信号、多重连接、装饰器用法等特性。
"""
class Calculator(QWidget):
    # 自定义信号
    calculation_done = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建布局
        main_layout = QVBoxLayout() # 主布局
        input_layout = QHBoxLayout() # 输入布局
        button_layout = QHBoxLayout() # 按钮布局

        # 创建控件
        self.num1_input = QLineEdit()
        self.num2_input = QLineEdit()
        self.result_label = QLabel('结果: ')
        self.history_label = QLabel('历史: ')

        add_button = QPushButton('+')
        subtract_button = QPushButton('-')
        multiply_button = QPushButton('*')
        divide_button = QPushButton('/')
        clear_button = QPushButton('清除')

        # 设置布局
        input_layout.addWidget(self.num1_input)
        input_layout.addWidget(self.num2_input)

        button_layout.addWidget(add_button)
        button_layout.addWidget(subtract_button)
        button_layout.addWidget(multiply_button)
        button_layout.addWidget(divide_button)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.history_label)
        main_layout.addWidget(clear_button)

        self.setLayout(main_layout)

        # 连接信号和槽
        add_button.clicked.connect(lambda: self.calculate('+'))
        subtract_button.clicked.connect(lambda: self.calculate('-'))
        multiply_button.clicked.connect(lambda: self.calculate('*'))
        divide_button.clicked.connect(lambda: self.calculate('/'))
        clear_button.clicked.connect(self.clear)

        # 使用装饰器连接自定义信号
        self.calculation_done.connect(self.update_history)

        # 多重连接示例
        for button in [add_button, subtract_button, multiply_button, divide_button]:
            button.clicked.connect(self.button_clicked)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('综合计算器示例')

    def calculate(self, operator):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ValueError("除数不能为零")
                result = num1 / num2
            
            self.result_label.setText(f'结果: {result}')
            # 发射自定义信号
            self.calculation_done.emit(f'{num1} {operator} {num2} = {result}')
        except ValueError as e:
            self.result_label.setText(f'错误: {str(e)}')

    @pyqtSlot()
    def clear(self):
        self.num1_input.clear()
        self.num2_input.clear()
        self.result_label.setText('结果: ')
        self.history_label.setText('历史: ')

    @pyqtSlot(str)
    def update_history(self, calculation):
        current_history = self.history_label.text()
        self.history_label.setText(f'{current_history}\n{calculation}')

    @pyqtSlot()
    def button_clicked(self):
        sender = self.sender()
        print(f'按钮 "{sender.text()}" 被点击了')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


"""

这个综合例子展示了以下特性：
自定义信号：calculation_done信号用于在计算完成时发出。
信号与槽的多种连接方式：
使用lambda函数连接：button.clicked.connect(lambda: self.calculate('+'))
使用装饰器连接：@pyqtSlot()
直接连接方法：clear_button.clicked.connect(self.clear)
信号的多重连接：所有运算按钮都连接到button_clicked方法。
参数传递：自定义信号calculation_done传递计算结果字符串。
5. 不同类型的槽函数：
无参数槽函数：clear()
带参数槽函数：update_history(calculation)
使用sender()方法识别信号发送者。
这个计算器示例综合了我们之前讨论的大多数信号与槽的概念。它允许用户输入两个数字，选择运算符进行计算，并显示结果和计算历史。
建议：
运行这个例子，尝试进行一些计算操作。
观察控制台输出，了解按钮点击的情况。
尝试修改代码，添加新的功能或信号连接。
思考如何进一步改进这个计算器，例如添加更多的运算符或实现连续计算。
"""