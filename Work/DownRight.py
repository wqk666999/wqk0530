from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class downright(QWidget):
    def __init__(self):
        super(downright, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.label_acc = QLabel('准确率:')
        self.textLine_acc = QLineEdit()
        self.label_f1 = QLabel('F1得分:')
        self.textLine_f1 = QLineEdit()
        self.label_recall = QLabel('召回率:')
        self.textLine_recall = QLineEdit()
        self.btu = QPushButton('运行输出')
        self.hbox.addStretch(0)
        self.hbox.addWidget(self.btu)
        self.hbox.addStretch(1)

        #self.showWidget = QTextBrowser()
        self.showWidget = QLabel()
        qfont = QFont()
        qfont.setPointSize(23)
        self.showWidget.setFont(qfont)
        self.showWidget.setEnabled(True)
        self.hbox1.addWidget(self.showWidget)
        self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label_acc)
        self.hbox2.addWidget(self.textLine_acc)
        self.hbox2.addWidget(self.label_recall)
        self.hbox2.addWidget(self.textLine_recall)
        self.hbox2.addWidget(self.label_f1)
        self.hbox2.addWidget(self.textLine_f1)
        self.hbox2.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)
        palette = QPalette()
        palette.setColor(self.showWidget.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.showWidget.setPalette(palette)
        self.showWidget.setAutoFillBackground(True)
