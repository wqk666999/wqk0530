# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kmeans_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import kmeans


class Kmeans_Window(QMainWindow):
    def __init__(self):
        super(Kmeans_Window, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("KmeansWindow")
        #self.resize(800, 600)
        self.setGeometry(100, 100, 500, 500)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 50, 71, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.get_trainfilePath)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 140, 281, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setEnabled(True)
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setSingleStep(1)
        self.spinBox.setProperty("value", 8)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_1.setEnabled(True)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setEnabled(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onclick_pushButton)
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(210, 380, 191, 71)   #QtCore.QRect
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setEnabled(False)
        self.textBrowser_2.setGeometry(QtCore.QRect(210, 50, 191, 23))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.comboBox_1.setCurrentIndex(0)

        screen = QDesktopWidget().screenGeometry()
        #   ?????????????????????
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

    def retranslateUi(self):
        self.pushButton_3.setText( "???????????????")
        self.label.setText("??????????????? n")
        self.label_2.setText( "???????????????")
        self.comboBox_1.setCurrentText( "k-means++")
        self.comboBox_1.setItemText(0, "k-means++")
        self.comboBox_1.setItemText(1, "random")
        self.comboBox_1.setItemText(2,  "ndarray")
        self.comboBox_1.setItemText(3,  "callable")
        self.label_4.setText( "??????")
        self.comboBox_3.setItemText(0, "auto")
        self.comboBox_3.setItemText(1,  "full")
        self.comboBox_3.setItemText(2, "elkan")
        self.pushButton.setText("???????????????")
        self.pushButton_2.setText("??????????????????")

    def get_trainfilePath(self):

        fname, _  = QFileDialog.getOpenFileName(self, 'Data file', '',"Data files (*.csv)")
        self.textBrowser_2.setEnabled(True)
        self.textBrowser_2.clear()
        self.textBrowser_2.setText(fname)
        #return fname

    def onclick_pushButton(self):
        n = self.spinBox.value()
        init = self.comboBox_1.currentText()
        algorithm = self.comboBox_3.currentText()
        options = {'n':n,
               'init':init,
               'algorithm':algorithm
                   }
        features = ['Formation','GR','ILD_log10','DeltaPHI','PHIND','PE','NM_M','RELPOS']
        trainpath =self.textBrowser_2.toPlainText()
        data = kmeans.data_process(trainpath,features)
        kmeans.train_useKmeans(data, options)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setText(f'???????????????????????????????????????')