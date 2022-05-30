import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import structure
import pandas as pd
import SVC_test
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class newMainWindow(QWidget):
    def __init__(self):
        super(newMainWindow, self).__init__()
        self.initUI()
        self.setObjectName('SVM')
    def initUI(self):
        self.topleft=structure.topleft()
        self.downleft=structure.downleft()
        #downleft.tab3UI()=tab3UI()
        self.topright=structure.topright()
        self.downright=structure.downright()
        self.tab3UI()
        # self.widget = QWidget()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.setWindowTitle('CIFLOg')
        self.setWindowState(Qt.WindowMaximized)
        #self.topleft = TopLeft.topleft()
        palette1 = QPalette()
        palette1.setColor(self.topleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topleft.setPalette(palette1)
        self.topleft.setAutoFillBackground(True)

        #downleft = SVC_DownLeft.downleft()
        palette2 = QPalette()
        palette2.setColor(self.downleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.downleft.setPalette(palette2)
        self.downleft.setAutoFillBackground(True)

        #self.topright = TopRight.topright()
        palette3 = QPalette()
        palette3.setColor(self.topright.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topright.setPalette(palette3)
        self.topright.setAutoFillBackground(True)

        #self.downright = DownRight.downright()
        palette4 = QPalette()
        palette4.setColor(self.downright.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.downright.setPalette(palette4)
        self.downright.setAutoFillBackground(True)

        self.splitter1 = QSplitter(Qt.Vertical)
        self.splitter1.addWidget(self.topleft)
        self.splitter1.addWidget(self.downleft)
        self.splitter1.setSizes([100, 200])
        self.vbox1.addWidget(self.splitter1)
        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.topright)
        self.splitter2.addWidget(self.downright)
        self.splitter2.setSizes([100,100])
        self.splitter3 = QSplitter(Qt.Horizontal)
        self.splitter3.addWidget(self.splitter1)
        self.splitter3.addWidget(self.splitter2)
        self.splitter3.setSizes([100,500])
        self.vbox2.addWidget(self.splitter2)
        self.hbox.addWidget(self.splitter3)
        self.setLayout(self.hbox)
        self.topleft.listwidget_train.clicked.connect(self.downleft_fea)
        #print('rrrrrrrrrrrrrrrrrrr'+self.topleft.listwidget_train.clicked)
        self.topleft.listwidget_val.clicked.connect(self.downleft_fea)
        self.topleft.listwidget_test.clicked.connect(self.downleft_fea)
        self.downleft.button_Run.clicked.connect(self.fun_Run)
    def tab3UI(self):
        vbox  = QVBoxLayout()
        hbox = QHBoxLayout()
        self.label_C = QLabel('惩罚系数C')
        self.label_C.setEnabled(True)
        self.spinBox_c = QDoubleSpinBox()
        self.spinBox_c.setEnabled(True)
        self.spinBox_c.setPrefix("")
        self.spinBox_c.setMinimum(0.0)
        self.spinBox_c.setMaximum(10.1)
        self.spinBox_c.setSingleStep(0.1)
        self.spinBox_c.setProperty("value", 1.0)
        self.spinBox_c.setObjectName("spinBox_c")
        self.label_kernal = QLabel("Kernal")
        self.label_kernal.setEnabled(True)
        self.combox_kernal = QComboBox()
        self.combox_kernal.setEnabled(True)
        self.combox_kernal.addItem("")
        self.combox_kernal.addItem("")
        self.combox_kernal.addItem("")
        self.combox_kernal.addItem("")
        self.combox_kernal.setCurrentText("rbf")
        self.combox_kernal.setItemText(0, "linear")
        self.combox_kernal.setItemText(1, "poly")
        self.combox_kernal.setItemText(2, "rbf")
        self.combox_kernal.setItemText(3, "sigmoid")
        self.label_gamma = QLabel("Gamma")
        self.label_gamma.setEnabled(True)
        self.combox_gamma = QComboBox()
        self.combox_gamma.setEnabled(True)
        self.combox_gamma.addItem("")
        self.combox_gamma.addItem("")
        self.combox_gamma.setItemText(0, "auto")
        self.combox_gamma.setItemText(1, "scale")
        self.label_DFS = QLabel("DFS")
        self.label_DFS.setEnabled(True)
        self.combox_DFS = QComboBox()
        self.combox_DFS.setEnabled(True)
        self.combox_DFS.addItem("")
        self.combox_DFS.addItem("")
        self.combox_DFS.setItemText(0, "ovr")
        self.combox_DFS.setItemText(1, "ovo")
        formLayout = QFormLayout()
        formLayout.addRow(self.label_C,self.spinBox_c)
        formLayout.addRow(self.label_kernal,self.combox_kernal)
        formLayout.addRow(self.label_gamma,self.combox_gamma)
        formLayout.addRow(self.label_DFS,self.combox_DFS)
        hbox.addLayout(formLayout)
        vbox.addLayout(hbox)
        self.downleft.tab3.setLayout(vbox)
        res={'spinBox_c':self.spinBox_c.value(),'combox_kernal':self.combox_kernal.currentText(),'combox_gamma':self.combox_gamma.currentText(),'combox_DFS':self.combox_DFS.currentText()}
        return res
    def downleft_fea(self):
        if self.topleft.tabWidget.currentWidget().objectName() == '训练数据':
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
            #print('rrrrrttttttttttttttttwwwww'+self.topleft.listwidget_train.currentItem().text())
            datafile = pd.read_csv('./data/' + self.topleft.listwidget_train.currentItem().text())
            self.downleft.data_train = self.topleft.listwidget_train.currentItem().text()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab1_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab2_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show2)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.showimage_topright)
        if self.topleft.tabWidget.currentWidget().objectName() == '验证数据':
            datafile = pd.read_csv('./data/' + self.topleft.listwidget_val.currentItem().text())
            self.downleft.data_val = self.topleft.listwidget_val.currentItem().text()
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab1_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab2_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show2)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.showimage_topright)
        if self.topleft.tabWidget.currentWidget().objectName() == '测试数据':
            datafile = pd.read_csv('./data/' + self.topleft.listwidget_test.currentItem().text())
            self.downleft.data_test = self.topleft.listwidget_test.currentItem().text()
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab1_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().deleteLater()
            for item in datafile.columns:
                checkbox = QCheckBox(item)
                self.downleft.layout_tab2_grid.addWidget(checkbox)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show)
            for i in range(self.downleft.layout_tab2_grid.count()):
                self.downleft.layout_tab2_grid.itemAt(i).widget().stateChanged.connect(
                    self.downleft.feaChecked_show2)
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().stateChanged.connect(
                    self.showimage_topright)
        QApplication.processEvents()

    def fun_Run(self):
        print('进入fun_Run函数')
        if (self.downleft.data_train != None) and (self.downleft.data_val != None) and (len(self.downleft.feature_selected) != 0) and (
                self.downleft.feature_pre != None):
            datafile_train = './data/' + self.downleft.data_train
            datafile_test = './data/' + self.downleft.data_val
            data_test = pd.read_csv(datafile_train)
            info=self.tab3UI()
            C=info['spinBox_c']
            kernel = info['combox_kernal']
            gamma = info['combox_gamma']
            decision_function_shape = info['combox_DFS']
            options = {'C': C,
                       'kernel': kernel, 'gamma': gamma,
                       'decision_function_shape': decision_function_shape
                       }
            data = SVC_test.data_process(datafile_train, datafile_test, self.downleft.feature_selected, self.downleft.feature_pre)
            res = SVC_test.train_useSVM(data, options)
            self.downright.textLine_acc.setText(str(res['acc']))
            self.downright.textLine_recall.setText(str(res['recall_score']))
            self.downright.textLine_f1.setText(str(res['f1_score']))
            print(str(res['confusion_matrix']))
            Png=QPixmap('SvmFacies_fig_270.png')
            self.downright.showWidget.setPixmap(Png)
            #self.downright.showWidget.setText(str(res['confusion_matrix']))
        print('退出fun_run函数')

    #def showimage_downright(self):
            
    def showimage_topright(self):
            for i in range(self.downleft.layout_tab1_grid.count()):
                if self.downleft.layout_tab1_grid.itemAt(i).widget().isChecked() == True:
                    # print(self.layout_tab1_grid.itemAt(i).widget().text())
                    self.topright.stack1.features_show.append(self.downleft.layout_tab1_grid.itemAt(i).widget().text())
            self.topright.stack1.initUI()
    #如果关闭了主窗体，则所有窗体都关闭
    def closeEvent(self, event):
        sys.exit(0)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    newmainwindow = newMainWindow()
    newmainwindow.show()
    sys.exit(app.exec_())
