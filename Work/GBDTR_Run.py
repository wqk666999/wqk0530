import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from numpy import double
import structure
import pandas as pd
import GBDTR_test

class newMainWindow(QWidget):
    def __init__(self):
        super(newMainWindow, self).__init__()
        self.initUI()
        self.setObjectName('GBDT')

    def initUI(self):
        # self.widget = QWidget()
        self.topleft=structure.topleft()
        self.downleft=structure.downleft()
        #downleft.tab3UI()=tab3UI()
        self.topright=structure.topright()
        self.downright=structure.downright()
        self.tab3UI()
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

       #self.downleft = GBDTR_DownLeft.downleft()
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
        self.topleft.listwidget_val.clicked.connect(self.downleft_fea)
        self.topleft.listwidget_test.clicked.connect(self.downleft_fea)
        self.downleft.button_Run.clicked.connect(self.fun_Run)
    def tab3UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.label_n_estimators = QLabel('n_estimators')
        self.label_n_estimators.setEnabled(True)
        self.spinBox = QDoubleSpinBox()
        self.spinBox.setEnabled(True)
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setSingleStep(2)
        self.spinBox.setProperty("value", 500)
        self.spinBox.setObjectName("spinBox")
        self.label_learning_rate = QLabel("learning_rate")
        self.label_learning_rate.setEnabled(True)
        self.combox_learning_rate = QComboBox()
        self.combox_learning_rate.setEnabled(True)
        self.combox_learning_rate.addItem("")
        self.combox_learning_rate.addItem("")
        self.combox_learning_rate.setCurrentText("0.1")
        self.combox_learning_rate.setItemText(0, "0.1")
        self.combox_learning_rate.setItemText(1, "0.01")
        self.label_max_depth = QLabel("max_depth")
        self.label_max_depth.setEnabled(True)
        self.combox_max_depth = QComboBox()
        self.combox_max_depth.setEnabled(True)
        self.combox_max_depth.addItem("")
        self.combox_max_depth.addItem("")
        self.combox_max_depth.addItem("")
        self.combox_max_depth.addItem("")
        self.combox_max_depth.setItemText(0, "12")
        self.combox_max_depth.setItemText(1, "13")
        self.combox_max_depth.setItemText(2, "14")
        self.combox_max_depth.setItemText(3, "15")
        self.label_max_leaf_nodes = QLabel("max_leaf_nodes")
        self.label_max_leaf_nodes.setEnabled(True)
        self.spinBox_max_leaf_nodes = QDoubleSpinBox()
        self.spinBox_max_leaf_nodes.setEnabled(True)
        self.spinBox_max_leaf_nodes.setPrefix("")
        self.spinBox_max_leaf_nodes.setMinimum(1)
        self.spinBox_max_leaf_nodes.setMaximum(99)
        self.spinBox_max_leaf_nodes.setProperty("value", 12)
        self.spinBox_max_leaf_nodes.setObjectName("spinBox_max_leaf_nodes")
        formLayout = QFormLayout()
        formLayout.addRow(self.label_n_estimators,self.spinBox)
        formLayout.addRow(self.label_learning_rate,self.combox_learning_rate)
        formLayout.addRow(self.label_max_depth,self.combox_max_depth)
        formLayout.addRow(self.label_max_leaf_nodes,self.spinBox_max_leaf_nodes)
        hbox.addLayout(formLayout)
        vbox.addLayout(hbox)
        self.downleft.tab3.setLayout(vbox)
        res={'spinBox':self.spinBox.value(),'combox_learning_rate':self.combox_learning_rate.currentText(),'combox_max_depth':self.combox_max_depth.currentText(),'spinBox_max_leaf_nodes':self.spinBox_max_leaf_nodes.value()}
        return res
    def downleft_fea(self):
        if self.topleft.tabWidget.currentWidget().objectName() == '训练数据':
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
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
            n_estimators = int(info['spinBox'])
            learning_rate = double(info['combox_learning_rate'])
            max_depth = int(info['combox_max_depth'])
            max_leaf_nodes = int(info['spinBox_max_leaf_nodes'])
            options = {'n_estimators': n_estimators,
                       'learning_rate': learning_rate, 'max_depth': max_depth,
                       'max_leaf_nodes': max_leaf_nodes
                       }
            data = GBDTR_test.data_process(datafile_train, datafile_test, self.downleft.feature_selected, self.downleft.feature_pre)
            res = GBDTR_test.train_useGBDT(data, options)
            self.downright.textLine_acc.setText(str(res['acc']))
            self.downright.textLine_recall.setText(str(res['recall_score']))
            self.downright.textLine_f1.setText(str(res['f1_score']))
            print(str(res['confusion_matrix']))
            Png=QPixmap('Gbdt_Facies_fig_270.png')
            self.downright.showWidget.setPixmap(Png)
        print('退出fun_run函数')
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
