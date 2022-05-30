from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import SVC_test

class downleft(QWidget):
    def __init__(self):
        super(downleft, self).__init__()
        self.initUI()
        self.data_train = None
        self.data_val = None
        self.data_test = None
        self.feature_pre = None
        self.feature_selected = []

    def initUI(self):

        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox = QHBoxLayout()
        self.button_Run = QPushButton()
        self.button_Run.setText('运行')
        self.tabWidget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabWidget.addTab(self.tab1, '输入特征')
        self.tabWidget.addTab(self.tab2, '预测目标')
        self.tabWidget.addTab(self.tab3, '模型参数')
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.button_Run)
        self.hbox1.addWidget(self.tabWidget)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def feaChecked_show(self):
        self.feature_selected = []
        for i in range(self.layout_tab1_grid.count()):
            if self.layout_tab1_grid.itemAt(i).widget().isChecked() == True:
                print(self.layout_tab1_grid.itemAt(i).widget().text())
                self.feature_selected.append(self.layout_tab1_grid.itemAt(i).widget().text())
        print('输入特征-------------------------------------------------------------')
    def feaChecked_show2(self):
        self.feature_pre = None
        for i in range(self.layout_tab2_grid.count()):
            if self.layout_tab2_grid.itemAt(i).widget().isChecked() == True:
                print(self.layout_tab2_grid.itemAt(i).widget().text())
                self.feature_pre = self.layout_tab2_grid.itemAt(i).widget().text()
        print('预测目标-------------------------------------------------------------')
    def tab1UI(self):
        self.layout_tab1 = QVBoxLayout()
        self.layout_tab1_grid = QGridLayout()
        self.layout_tab1.addStretch(0)
        self.layout_tab1.addLayout(self.layout_tab1_grid)
        self.layout_tab1.addStretch(1)
        self.tab1.setLayout(self.layout_tab1)
    def tab2UI(self):
        self.layout_tab2 = QVBoxLayout()
        self.layout_tab2_grid = QGridLayout()
        self.layout_tab2.addStretch(0)
        self.layout_tab2.addLayout(self.layout_tab2_grid)
        self.layout_tab2.addStretch(1)
        self.tab2.setLayout(self.layout_tab2)
    def tab3UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.label_layers = QLabel('堆叠层数')
        self.label_layers.setEnabled(True)
        self.spinBox_layers = QSpinBox()
        self.spinBox_layers.setEnabled(True)
        self.spinBox_layers.setPrefix("")
        self.spinBox_layers.setMinimum(1)
        # self.spinBox.setMaximum(10.1)
        self.spinBox_layers.setSingleStep(1)
        self.spinBox_layers.setProperty("value", 1)
        self.spinBox_layers.setObjectName("spinBox")
        self.label_units = QLabel("units")
        self.label_units.setEnabled(True)
        self.spinBox_units = QSpinBox()
        self.spinBox_units.setEnabled(True)
        self.spinBox_units.setPrefix("")
        self.spinBox_units.setMinimum(1)
        self.spinBox_units.setSingleStep(1)
        self.spinBox_units.setProperty("value",6)
        self.label_kernel_regularizer = QLabel("kernel_initializer")
        self.label_kernel_regularizer.setEnabled(True)
        self.combox_kernel_regularizer = QComboBox()
        self.combox_kernel_regularizer.setEnabled(True)
        self.combox_kernel_regularizer.addItem("")
        self.combox_kernel_regularizer.addItem("")
        self.combox_kernel_regularizer.setCurrentText("l2")
        self.combox_kernel_regularizer.setItemText(0, "l1")
        self.combox_kernel_regularizer.setItemText(1, "l2")
        # self.combox_kernel_regularizer.setItemText(2, "rbf")
        # self.combox_kernel_regularizer.setItemText(3, "sigmoid")
        self.label_dropout = QLabel("dropout")
        self.label_dropout.setEnabled(True)
        self.spinBox_dropout = QDoubleSpinBox()
        self.spinBox_dropout.setEnabled(True)
        self.spinBox_dropout.setPrefix("")
        self.spinBox_dropout.setMinimum(0.1)
        self.spinBox_dropout.setMaximum(0.9)
        self.spinBox_dropout.setSingleStep(0.1)
        self.spinBox_dropout.setProperty("value", 0.5)
        self.spinBox_dropout.setObjectName("spinBox_dropout")
        self.label_use_bias = QLabel("use_bias")
        self.label_use_bias.setEnabled(True)
        self.combox_use_bias = QComboBox()
        self.combox_use_bias.setEnabled(True)
        self.combox_use_bias.addItem("")
        self.combox_use_bias.addItem("")
        self.combox_use_bias.setItemText(0, "True")
        self.combox_use_bias.setItemText(1, "False")

        formLayout = QFormLayout()
        formLayout.addRow(self.label_layers,self.spinBox_layers)
        formLayout.addRow(self.label_units,self.spinBox_units)
        formLayout.addRow(self.label_kernel_regularizer,self.combox_kernel_regularizer)
        formLayout.addRow(self.label_dropout,self.spinBox_dropout)
        formLayout.addRow(self.label_use_bias, self.combox_use_bias)
        # formLayout.addRow(self.label_dropout, self.spinBox_dropout)
        hbox.addLayout(formLayout)
        vbox.addLayout(hbox)
        self.tab3.setLayout(vbox)

