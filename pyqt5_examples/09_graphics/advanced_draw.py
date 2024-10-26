#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyQt5绘图综合示例
总结：
1. 功能描述：
   - 展示PyQt5各种绘图能力
   - 包含基础图形绘制、文本、渐变、变换等
   - 实现简单的交互效果

2. 类设计：
   - AdvancedDrawingDemo: 主窗口类，包含多个独立的绘图演示函数
   - 每个绘图函数专注于展示一个特定的绘图特性

3. 关键技术点：
   - QPainter基础和高级用法
   - 渐变和变换
   - 自定义图形项
   - 动画效果

4. 展示的控件种类：
   - QWidget: 基础窗口控件
   - QLabel: 标签控件，用于显示文本
   - QGridLayout: 网格布局，用于管理控件的布局
   - QVBoxLayout: 垂直布局，用于管理控件的布局

5. 用到的技术：
   - QPainter: 绘图设备类，用于在控件上进行绘图
   - QPen: 画笔类，用于设置绘图的线条样式
   - QColor: 颜色类，用于设置绘图的颜色
   - QLinearGradient: 线性渐变类，用于创建线性渐变效果
   - QConicalGradient: 圆锥渐变类，用于创建圆锥渐变效果
   - QPainterPath: 绘图路径类，用于创建复杂的绘图路径
   - QFont: 字体类，用于设置文本的字体
   - QTimer: 定时器类，用于创建动画效果
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout
from PyQt5.QtGui import (QPainter, QPen, QColor, QLinearGradient, QPainterPath, QFont, QConicalGradient)
from PyQt5.QtCore import Qt, QRectF, QTimer

class DrawingArea(QWidget):
    def __init__(self, draw_function):
        super().__init__()
        self.draw_function = draw_function

    def paintEvent(self, event):
        # 创建QPainter对象
        painter = QPainter(self)
        # 设置抗锯齿渲染提示
        painter.setRenderHint(QPainter.Antialiasing)
        try:
            # 调用绘图函数
            self.draw_function(painter, self.rect())
        except Exception as e:
            # 捕获并打印异常信息
            import traceback
            traceback.print_exc()

class DrawingWidget(QWidget):
    """
    绘图小部件类，用于展示绘图函数
    """
    def __init__(self, draw_function, label_text):
        super().__init__()

        # 创建并设置标签
        self.label = QLabel(label_text)
        self.label.setAlignment(Qt.AlignCenter)

        # 创建绘图区域
        self.drawing_area = DrawingArea(draw_function)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.drawing_area)

        self.setLayout(layout)

class AdvancedDrawingDemo(QWidget):
    """
    高级绘图示例主窗口类
    """
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupAnimationParameters()
    
    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('PyQt5绘图示例')
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(palette)

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        drawing_widgets = [
            ("复杂路径", self.drawComplexPath),
            ("圆锥渐变", self.drawConicalGradient),
            ("图形组合", self.drawCompositionMode),
            ("裁剪效果", self.drawClipping),
            ("阴影效果", self.drawShadowEffect),
            ("图形变换", self.drawTransformation),
            ("渐变路径", self.drawGradientPath),
            ("自定义画笔", self.drawCustomPenStyles),
            ("文本特效", self.drawTextEffects)
        ]

        for i, (label, func) in enumerate(drawing_widgets):
            try:
                widget = DrawingWidget(func, label)
                grid_layout.addWidget(widget, i // 3, i % 3)
            except Exception as e:
                import traceback
                traceback.print_exc()

    def setupAnimationParameters(self):
        """
        设置动画参数
        """
        self.angle = 0
        self.scale_factor = 1.0
        self.scale_increasing = True
        self.text_angle = 0
        self.dash_offset = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(50)
        print("Animation parameters set up completed")

    def updateAnimation(self):
        """
        更新动画
        """
        self.angle = (self.angle + 2) % 360
        if self.scale_increasing:
            self.scale_factor += 0.02
            if self.scale_factor >= 1.5:
                self.scale_increasing = False
        else:
            self.scale_factor -= 0.02
            if self.scale_factor <= 0.5:
                self.scale_increasing = True
        self.text_angle = (self.text_angle + 1) % 360
        self.dash_offset = (self.dash_offset + 1) % 20
        self.update()
        # print("Animation updated")  # 根据需要取消注释

    # 以下是各个绘图函数，每个函数专注于一种特定的绘图效果

    def drawComplexPath(self, painter, rect):
        """
        绘制复杂路径
        """
        painter.save()
        path = QPainterPath()
        path.moveTo(rect.left(), rect.center().y())
        path.cubicTo(
            rect.left() + rect.width()*0.3, rect.top(),
            rect.left() + rect.width()*0.7, rect.bottom(),
            rect.right(), rect.center().y()
        )
        painter.setPen(QPen(Qt.blue, 2))
        painter.drawPath(path)
        painter.restore()

    def drawConicalGradient(self, painter, rect):
        """
        绘制圆锥渐变
        """
        painter.save()
        center = rect.center()
        conicalGradient = QConicalGradient(center, self.angle)
        conicalGradient.setColorAt(0, Qt.red)
        conicalGradient.setColorAt(0.5, Qt.green)
        conicalGradient.setColorAt(1, Qt.blue)
        painter.setBrush(conicalGradient)
        painter.setPen(Qt.NoPen)  # 添加这行
        painter.drawEllipse(rect.adjusted(10, 10, -10, -10))  # 修改这行
        painter.restore()

    def drawCompositionMode(self, painter, rect):
        """
        绘制图形组合示例
        """
        painter.save()
        painter.translate(rect.topLeft())
        painter.scale(rect.width() / 200, rect.height() / 200)
        painter.setBrush(Qt.red)
        painter.drawEllipse(0, 0, 100, 100)
        painter.setCompositionMode(QPainter.CompositionMode_Multiply)
        painter.setBrush(Qt.blue)
        painter.drawEllipse(50, 0, 100, 100)
        painter.restore()

    def drawClipping(self, painter, rect):
        """
        绘制最基本的裁剪示例
        """
        painter.save()
        
        # 创建圆形裁剪路径
        center = rect.center()
        radius = min(rect.width(), rect.height()) / 2 - 10
        clipPath = QPainterPath()
        clipPath.addEllipse(center, radius, radius)
        
        # 设置裁剪路径
        painter.setClipPath(clipPath)
        
        # 绘制背景
        painter.fillRect(rect, Qt.lightGray)
        
        # 绘制一些线条
        painter.setPen(QPen(Qt.black, 2))
        painter.drawLine(rect.topLeft(), rect.bottomRight())
        painter.drawLine(rect.topRight(), rect.bottomLeft())
        
        # 绘制一个矩形
        painter.setBrush(Qt.red)
        painter.drawRect(rect.adjusted(20, 20, -20, -20))
        
        painter.restore()
        print("Basic clipping drawn")

    def drawShadowEffect(self, painter, rect):
        """
        绘制阴影效果
        """
        painter.save()
        shadow_color = QColor(0, 0, 0, 100)
        painter.setPen(Qt.NoPen)
        painter.setBrush(shadow_color)
        painter.translate(rect.center())
        painter.drawEllipse(-25, 5, 60, 60)  # 阴影
        painter.setBrush(Qt.yellow)
        painter.drawEllipse(-30, -10, 60, 60)  # 主图形
        painter.restore()
        print("Shadow effect drawn")

    def drawTransformation(self, painter, rect):
        """
        绘制图形变换示例
        """
        painter.save()
        painter.translate(rect.center())
        painter.rotate(self.angle)
        painter.scale(self.scale_factor, self.scale_factor)
        painter.shear(0.2, 0.2)
        painter.setPen(QPen(Qt.red, 2))
        painter.drawRect(-25, -25, 50, 50)
        painter.restore()
        print("Transformation drawn")

    def drawGradientPath(self, painter, rect):
        """
        绘制渐变路径
        """
        painter.save()
        path = QPainterPath()
        path.moveTo(rect.left(), rect.center().y())
        path.quadTo(rect.center().x(), rect.top(), rect.right(), rect.center().y())
        path.quadTo(rect.center().x(), rect.bottom(), rect.left(), rect.center().y())

        gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
        gradient.setColorAt(0, QColor(255, 0, 0, 200))
        gradient.setColorAt(0.5, QColor(0, 255, 0, 150))
        gradient.setColorAt(1, QColor(0, 0, 255, 200))

        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)
        painter.restore()

    def drawCustomPenStyles(self, painter, rect):
        """
        绘制自定义画笔样式
        """
        painter.save()
        pen = QPen(Qt.darkBlue, 3)
        pen.setDashPattern([8, 4, 2, 4])
        pen.setDashOffset(self.dash_offset)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)
        painter.drawLine(rect.left(), rect.center().y(), rect.right(), rect.center().y())
        painter.drawRect(rect.adjusted(20, 20, -20, -20))
        painter.restore()

    def drawTextEffects(self, painter, rect):
        """
        绘制文本特效
        """
        painter.save()
        # 旋转文本
        painter.translate(rect.center())
        painter.rotate(self.text_angle)
        font = QFont('Arial', 12)
        painter.setFont(font)
        painter.drawText(QRectF(-50, -50, 100, 100), Qt.AlignCenter, "Rotating")
        painter.resetTransform()

        # 路径文本
        path = QPainterPath()
        font = QFont('Times', 12)
        path.addText(rect.left() + 10, rect.bottom() - 10, font, "Path Text")
        painter.setPen(QPen(Qt.blue, 1))
        painter.setBrush(QColor(255, 0, 0, 100))
        painter.drawPath(path)

        # 文本阴影
        painter.setPen(QColor(0, 0, 0, 100))
        painter.drawText(QRectF(rect.left() + 2, rect.top() + 2, 100, 30), Qt.AlignCenter, "Shadow")
        painter.setPen(Qt.black)
        painter.drawText(QRectF(rect.left(), rect.top(), 100, 30), Qt.AlignCenter, "Shadow")
        painter.restore()
        print("Text effects drawn")

def main():
    app = QApplication(sys.argv)
    try:
        demo = AdvancedDrawingDemo()
        demo.show()
        sys.exit(app.exec_())
    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
