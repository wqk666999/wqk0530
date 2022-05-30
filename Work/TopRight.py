from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ShowImage_TopRight


class topright(QWidget):
    def __init__(self):
        super(topright, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.label1 = QLabel('测井曲线显示')
        self.label2 = QLabel('')
        self.label3 = QLabel('')
        self.label4 = QLabel('')
        self.hbox1.addStretch(0)
        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.label2)
        self.hbox1.addWidget(self.label3)
        self.hbox1.addWidget(self.label4)
        self.hbox1.addStretch(1)
        self.btuWidget = QWidget()
        self.button1 = QPushButton('训练数据')
        self.button2 = QPushButton('验证数据')
        self.button3 = QPushButton('测试数据')
        self.butVbox = QVBoxLayout()
        self.butVbox.addStretch(0)
        self.butVbox.addWidget(self.button1)
        self.butVbox.addWidget(self.button2)
        self.butVbox.addWidget(self.button3)
        self.butVbox.addStretch(1)
        self.btuWidget.setLayout(self.butVbox)

        self.stack = QStackedWidget()
        self.stack1 = ShowImage_TopRight.ApplicationWindow()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.hbox2.addWidget(self.btuWidget)
        self.hbox2.addWidget(self.stack)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        palette = QPalette()
        palette.setColor(self.btuWidget.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.btuWidget.setPalette(palette)
        self.btuWidget.setAutoFillBackground(True)
        palette1 = QPalette()
        palette.setColor(self.stack1.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.stack1.setPalette(palette)
        self.stack1.setAutoFillBackground(True)
        palette2 = QPalette()
        palette.setColor(self.stack2.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.stack2.setPalette(palette)
        self.stack2.setAutoFillBackground(True)
        palette3 = QPalette()
        palette.setColor(self.stack3.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.stack3.setPalette(palette)
        self.stack3.setAutoFillBackground(True)

    def tab1UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.stack1.label = QLabel('训练数据')
        hbox.addWidget(self.stack1.label)

        vbox.addLayout(hbox)
        self.stack1.setLayout(vbox)
    def tab2UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.stack2.label = QLabel('验证数据')
        hbox.addWidget(self.stack2.label)

        vbox.addLayout(hbox)
        self.stack2.setLayout(vbox)
    def tab3UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.stack3.label = QLabel('测试数据')
        hbox.addWidget(self.stack3.label)

        vbox.addLayout(hbox)
        self.stack3.setLayout(vbox)
