import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import structure
import pandas as pd
import KNN_test

class newMainWindow(QWidget):
    def __init__(self):
        super(newMainWindow, self).__init__()
        self.initUI()
        self.setObjectName('KNN')

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
       # self.topleft = TopLeft.topleft()
        palette1 = QPalette()
        palette1.setColor(self.topleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topleft.setPalette(palette1)
        self.topleft.setAutoFillBackground(True)

        #self.downleft = KNN_DownLeft.downleft()
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
    def tab3UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.label_n_neighbors = QLabel('n_neighbors')
        self.label_n_neighbors.setEnabled(True)
        self.spinBox_neighbors = QDoubleSpinBox()
        self.spinBox_neighbors.setEnabled(True)
        self.spinBox_neighbors.setPrefix("")
        self.spinBox_neighbors.setMinimum(1)
        self.spinBox_neighbors.setMaximum(99)
        self.spinBox_neighbors.setSingleStep(1)
        self.spinBox_neighbors.setProperty("value", 5)
        self.spinBox_neighbors.setObjectName("spinBox_neighbors")
        self.label_weights = QLabel("weights")
        self.label_weights.setEnabled(True)
        self.combox_weights = QComboBox()
        self.combox_weights.setEnabled(True)
        self.combox_weights.addItem("")
        self.combox_weights.addItem("")
        self.combox_weights.setCurrentText("uniform")
        self.combox_weights.setItemText(0, "uniform")
        self.combox_weights.setItemText(1, "distance")
        self.label_algorithm = QLabel("algorithm")
        self.label_algorithm.setEnabled(True)
        self.combox_algorithm = QComboBox()
        self.combox_algorithm.setEnabled(True)
        self.combox_algorithm.addItem("")
        self.combox_algorithm.addItem("")
        self.combox_algorithm.addItem("")
        self.combox_algorithm.addItem("")
        self.combox_algorithm.setItemText(0, "auto")
        self.combox_algorithm.setItemText(1, "ball_tree")
        self.combox_algorithm.setItemText(2, "kd_tree")
        self.combox_algorithm.setItemText(3, "brute")
        self.label_leaf_size = QLabel("leaf_size")
        self.label_leaf_size.setEnabled(True)
        self.spinBox_leaf_size = QSpinBox()
        self.spinBox_leaf_size.setEnabled(True)
        self.spinBox_leaf_size.setPrefix("")
        self.spinBox_leaf_size.setMinimum(1)
        self.spinBox_leaf_size.setMaximum(99)
        self.spinBox_leaf_size.setProperty("value", 30)
        self.spinBox_leaf_size.setObjectName("spinBox_leaf_size")
        # self.combox_DFS = QComboBox()
        # self.combox_DFS.setEnabled(True)
        # self.combox_DFS.addItem("")
        # self.combox_DFS.addItem("")
        # self.combox_DFS.setItemText(0, "ovr")
        # self.combox_DFS.setItemText(1, "ovo")
        formLayout = QFormLayout()
        formLayout.addRow(self.label_n_neighbors,self.spinBox_neighbors)
        formLayout.addRow(self.label_weights,self.combox_weights)
        formLayout.addRow(self.label_algorithm,self.combox_algorithm)
        formLayout.addRow(self.label_leaf_size,self.spinBox_leaf_size)
        hbox.addLayout(formLayout)
        vbox.addLayout(hbox)
        self.downleft.tab3.setLayout(vbox)
        res={'spinBox_neighbors':self.spinBox_neighbors.value(),'combox_weights':self.combox_weights.currentText(),'combox_algorithm':self.combox_algorithm.currentText(),'spinBox_leaf_size':self.spinBox_leaf_size.value()}
        return res
    def fun_Run(self):
        print('进入fun_Run函数')
        if (self.downleft.data_train != None) and (self.downleft.data_val != None) and (len(self.downleft.feature_selected) != 0) and (
                self.downleft.feature_pre != None):
            datafile_train = './data/' + self.downleft.data_train
            datafile_test = './data/' + self.downleft.data_val
            data_test = pd.read_csv(datafile_train)
            info=self.tab3UI()
            n_neighbors = int(info['spinBox_neighbors'])
            weights = info['combox_weights']
            algorithm = info['combox_algorithm']
            leaf_size = int(info['spinBox_leaf_size'])
            options = {'n_neighbors': n_neighbors,
                       'weights': weights, 'algorithm': algorithm,
                       'leaf_size': leaf_size
                       }
            data = KNN_test.data_process(datafile_train, datafile_test, self.downleft.feature_selected, self.downleft.feature_pre)
            res = KNN_test.train_useKNN(data, options)
            self.downright.textLine_acc.setText(str(res['acc']))
            self.downright.textLine_recall.setText(str(res['recall_score']))
            self.downright.textLine_f1.setText(str(res['f1_score']))
            print(str(res['confusion_matrix']))
            Png=QPixmap('SvmFacies_fig_270.png')
            self.downright.showWidget.setPixmap(Png)
            #self.downright.showWidget.setText(str(res["confusion_matrix"]))
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
