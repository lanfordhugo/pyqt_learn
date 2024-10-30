#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyQt5高级绘图示例 - 模拟时钟
功能特点：
1. 精美的表盘设计
2. 平滑的指针动画
3. 光影效果
4. 刻度和数字显示
5. 日期显示
6. 装饰效果

总结：
1. 用到的技术：
   - QPainter: 绘图设备类，用于在控件上进行绘图
   - QPen: 画笔类，用于设置绘图的线条样式
   - QBrush: 画刷类，用于设置填充样式
   - QColor: 颜色类，用于设置绘图的颜色
   - QLinearGradient: 线性渐变类，用于创建线性渐变效果
   - QRadialGradient: 辐射渐变类，用于创建辐射渐变效果
   - QPainterPath: 绘图路径类，用于创建复杂的绘图路径
   - QFont: 字体类，用于设置文本的字体
   - QFontMetrics: 字体度量类，用于测量文本尺寸
   - QTimer: 定时器类，用于创建动画效果
   - QPoint: 点类，用于表示二维空间中的点
   - QRect: 矩形类，用于表示矩形区域
   - QPointF: 浮点型点类，用于表示二维空间中的浮点型点
"""

import sys
import time
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import (QPainter, QPen, QBrush, QColor, QLinearGradient,
                        QRadialGradient, QPainterPath, QFont, QFontMetrics)
from PyQt5.QtCore import Qt, QTimer, QPoint, QRect, QPointF

class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # 初始化定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # 每秒更新一次
        
    def initUI(self):
        """初始化UI"""
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('模拟时钟')
        # 设置背景色
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(palette)
        
    def paintEvent(self, event):
        """绘制事件"""
        # 获取当前时间
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        
        # 创建画家
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 计算中心点和半径
        center = self.rect().center()
        radius = min(self.width(), self.height()) // 2 - 10
        
        # 1. 绘制表盘底色和边框
        self.drawClockFace(painter, center, radius)
        
        # 2. 绘制刻度
        self.drawScale(painter, center, radius)
        
        # 3. 绘制数字
        self.drawNumbers(painter, center, radius)
        
        # 4. 绘制指针
        self.drawHands(painter, center, radius, hours, minutes, seconds)
        
        # 5. 绘制中心点
        self.drawCenter(painter, center)
        
        # 6. 绘制日期
        self.drawDate(painter, center, radius)
        
    def drawClockFace(self, painter, center, radius):
        """绘制表盘"""
        painter.save()
        
        # 创建径向渐变
        gradient = QRadialGradient(center, radius)
        gradient.setColorAt(0, QColor(240, 240, 240))
        gradient.setColorAt(0.8, QColor(220, 220, 220))
        gradient.setColorAt(1, QColor(200, 200, 200))
        
        # 绘制表盘底色
        painter.setPen(Qt.NoPen)
        painter.setBrush(gradient)
        painter.drawEllipse(center, radius, radius)
        
        # 绘制表盘边框
        painter.setPen(QPen(QColor(150, 150, 150), 2))
        painter.drawEllipse(center, radius, radius)
        
        painter.restore()
        
    def drawScale(self, painter, center, radius):
        """绘制刻度"""
        painter.save()
        
        painter.translate(center)
        for i in range(60):
            if i % 5 == 0:
                # 主刻度
                painter.setPen(QPen(Qt.black, 2))
                painter.drawLine(0, -(radius-10), 0, -(radius-30))
            else:
                # 次刻度
                painter.setPen(QPen(Qt.black, 1))
                painter.drawLine(0, -(radius-15), 0, -(radius-25))
            painter.rotate(6)  # 360/60=6度
            
        painter.restore()
        
    def drawNumbers(self, painter, center, radius):
        """绘制数字"""
        painter.save()
        
        font = QFont('Arial', radius//10)
        font.setBold(True)
        painter.setFont(font)
        
        for i in range(1, 13):
            angle = i * 30  # 360/12=30度
            x = center.x() + (radius-60) * math.sin(math.radians(angle))
            y = center.y() - (radius-60) * math.cos(math.radians(angle))
            
            # 计算文本矩形
            text = str(i)
            fm = QFontMetrics(font)
            text_rect = fm.boundingRect(text)
            
            # 使用 QPointF 来处理浮点数坐标
            text_position = QPointF(
                x - text_rect.width()/2,
                y + text_rect.height()/2
            )
            
            painter.drawText(text_position, text)
        
        painter.restore()
        
    def drawHands(self, painter, center, radius, hours, minutes, seconds):
        """绘制指针"""
        painter.save()
        painter.translate(center)
        
        # 时针
        hour_angle = (hours + minutes/60) * 30  # 360/12=30度
        painter.save()
        painter.rotate(hour_angle)
        self.drawHourHand(painter, radius * 0.5)
        painter.restore()
        
        # 分针
        minute_angle = minutes * 6  # 360/60=6度
        painter.save()
        painter.rotate(minute_angle)
        self.drawMinuteHand(painter, radius * 0.7)
        painter.restore()
        
        # 秒针
        second_angle = seconds * 6  # 360/60=6度
        painter.save()
        painter.rotate(second_angle)
        self.drawSecondHand(painter, radius * 0.8)
        painter.restore()
        
        painter.restore()
        
    def drawHourHand(self, painter, length):
        """绘制时针"""
        path = QPainterPath()
        path.moveTo(QPointF(-2, 0))
        path.lineTo(QPointF(2, 0))
        path.lineTo(QPointF(1, -length))
        path.lineTo(QPointF(-1, -length))
        path.closeSubpath()
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(80, 80, 80))
        painter.drawPath(path)
        
    def drawMinuteHand(self, painter, length):
        """绘制分针"""
        path = QPainterPath()
        path.moveTo(QPointF(-1.5, 0))
        path.lineTo(QPointF(1.5, 0))
        path.lineTo(QPointF(0.8, -length))
        path.lineTo(QPointF(-0.8, -length))
        path.closeSubpath()
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(50, 50, 50))
        painter.drawPath(path)
        
    def drawSecondHand(self, painter, length):
        """绘制秒针"""
        painter.setPen(QPen(Qt.red, 1))
        # 将浮点数转换为整数
        painter.drawLine(0, 0, 0, int(-length))
        
    def drawCenter(self, painter, center):
        """绘制中心点"""
        painter.save()
        
        # 绘制外圈
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(120, 120, 120))
        # 使用整数半径
        painter.drawEllipse(center, int(8), int(8))
        
        # 绘制内圈
        painter.setBrush(Qt.red)
        painter.drawEllipse(center, int(4), int(4))
        
        painter.restore()
        
    def drawDate(self, painter, center, radius):
        """绘制日期"""
        painter.save()
        
        current_date = time.strftime("%Y-%m-%d")
        font = QFont('Arial', radius//20)
        painter.setFont(font)
        
        fm = QFontMetrics(font)
        text_rect = fm.boundingRect(current_date)
        
        # 使用 QPointF 来处理浮点数坐标
        text_position = QPointF(
            center.x() - text_rect.width()/2,
            center.y() + radius/2
        )
        
        painter.drawText(text_position, current_date)
        
        painter.restore()

def main():
    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

