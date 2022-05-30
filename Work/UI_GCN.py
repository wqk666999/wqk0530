
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Ui_MainWindow(object):

    def setupUi(self, MainWindow,num):
        info_name=[]
        info_values=[]
        self.num = num
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        for i in range(self.num):
            exec('self.label1_{} = QtWidgets.QLabel(self.centralwidget)'.format(str(i)))
            exec("self.label1_{}.setGeometry(QtCore.QRect(30, 80+{}, 72, 15))".format(i,i*30))
            exec('self.label1_{}.setObjectName("label1_{}")'.format(i,i))

            exec('self.label2_{} = QtWidgets.QLabel(self.centralwidget)'.format(i))
            exec('self.label2_{}.setGeometry(QtCore.QRect(260, 80+{}, 72, 15))'.format(i,i*30))
            exec('self.label2_{}.setObjectName("label_2_{}")'.format(i,i))

            exec('self.pushButton_{} = QtWidgets.QPushButton(self.centralwidget)'.format(i))
            exec('self.pushButton_{}.setGeometry(QtCore.QRect(460, 80+{}, 93, 28))'.format(i,i*30))
            exec('self.pushButton_{}.setObjectName("pushButton_{}")'.format(i,i))

            exec('self.lineEdit1_{} = QtWidgets.QComboBox(self.centralwidget)'.format(i))
            exec('self.lineEdit1_{}.setEnabled(True)'.format(i))
            exec('self.lineEdit1_{}.addItem("")'.format(i))
            exec('self.lineEdit1_{}.addItem("")'.format(i))
            exec('self.lineEdit1_{}.setCurrentText("Li-GCN")'.format(i))
            exec('self.lineEdit1_{}.setItemText(0, "Li-GCN")'.format(i))
            exec('self.lineEdit1_{}.setItemText(1, "XXXX")'.format(i))
            exec('self.lineEdit1_{}.setGeometry(QtCore.QRect(90, 80+{}, 113, 21))'.format(i,i*30))
            exec('self.lineEdit1_{}.setObjectName("lineEdit1_{}")'.format(i,i))
            
            #combox_kernal.currentText()
            exec('self.lineEdit2_{} = QtWidgets.QLineEdit(self.centralwidget)'.format(i))
            exec('self.lineEdit2_{}.setGeometry(QtCore.QRect(310, 80+{}, 113, 21))'.format(i,i*30))
            exec('self.lineEdit2_{}.setObjectName("lineEdit2_{}")'.format(i,i))
            #exec('self.info_values.append(self.lineEdit2_{}.value())'.format(i))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_run.setObjectName('yunxing')
        # self.pushButton_run.setText("提交")
        # self.pushButton_run.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        for i in range(self.num):
            exec('self.label1_{}.setText(_translate("MainWindow", "层类型："))'.format(i))
            print(exec('self.lineEdit1_{}.currentText()'.format(i)))
            exec('self.label2_{}.setText(_translate("MainWindow", "神经元数："))'.format(i))
            exec('self.pushButton_{}.setText(_translate("MainWindow", "add"))'.format(i))
            exec('self.pushButton_{}.clicked.connect(MainWindow.add)'.format(i))



