import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import structure
import pandas as pd
import XGBoost_test

class newMainWindow(QWidget):
    def __init__(self):
        super(newMainWindow, self).__init__()
        self.initUI()
        self.setObjectName('XGBoost')

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
#        self.topleft = TopLeft.topleft()
        palette1 = QPalette()
        palette1.setColor(self.topleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topleft.setPalette(palette1)
        self.topleft.setAutoFillBackground(True)

      #  self.downleft = XGBoost_DownLeft.downleft()
        palette2 = QPalette()
        palette2.setColor(self.downleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.downleft.setPalette(palette2)
        self.downleft.setAutoFillBackground(True)

       # self.topright = TopRight.topright()
        palette3 = QPalette()
        palette3.setColor(self.topright.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topright.setPalette(palette3)
        self.topright.setAutoFillBackground(True)

       # self.downright = DownRight.downright()
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
        self.label_learning_rate = QLabel('learning_rate')
        self.label_learning_rate.setEnabled(True)
        self.spinBox = QDoubleSpinBox()
        self.spinBox.setEnabled(True)
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(0.0)
        self.spinBox.setMaximum(10.1)
        self.spinBox.setSingleStep(0.1)
        self.spinBox.setProperty("value", 0.01)
        self.spinBox.setObjectName("spinBox")
        self.label_n_estimators = QLabel('n_estimators')
        self.label_n_estimators.setEnabled(True)
        self.spinBox_n_estimators = QSpinBox()
        self.spinBox_n_estimators.setEnabled(True)
        self.spinBox_n_estimators.setPrefix("")
        self.spinBox_n_estimators.setMinimum(0)
        self.spinBox_n_estimators.setMaximum(100)
        self.spinBox_n_estimators.setSingleStep(1)
        self.spinBox_n_estimators.setProperty("value", 10)
        self.spinBox_n_estimators.setObjectName("spinBox_n_estimators")
        self.label_max_depth = QLabel('max_depth')
        self.label_max_depth.setEnabled(True)
        self.spinBox_max_depth = QSpinBox()
        self.spinBox_max_depth.setEnabled(True)
        self.spinBox_max_depth.setPrefix("")
        self.spinBox_max_depth.setMinimum(0)
        self.spinBox_max_depth.setMaximum(100)
        self.spinBox_max_depth.setSingleStep(1)
        self.spinBox_max_depth.setProperty("value", 4)
        self.spinBox_max_depth.setObjectName("spinBox_max_depth")
        self.label_min_child_weight  = QLabel('min_child_weight ')
        self.label_min_child_weight .setEnabled(True)
        self.spinBox_min_child_weight = QSpinBox()
        self.spinBox_min_child_weight.setEnabled(True)
        self.spinBox_min_child_weight.setPrefix("")
        self.spinBox_min_child_weight.setMinimum(1)
        self.spinBox_min_child_weight.setMaximum(10)
        self.spinBox_min_child_weight.setSingleStep(1)
        self.spinBox_min_child_weight.setProperty("value", 1)
        self.spinBox_min_child_weight.setObjectName("spinBox_min_child_weight ")
        self.label_gamma = QLabel('gamma')
        self.label_gamma.setEnabled(True)
        self.spinBox_gamma  = QSpinBox()
        self.spinBox_gamma.setEnabled(True)
        self.spinBox_gamma.setPrefix("")
        self.spinBox_gamma.setMinimum(0)
        self.spinBox_gamma.setMaximum(10)
        self.spinBox_gamma.setSingleStep(1)
        self.spinBox_gamma.setProperty("value", 0)
        self.spinBox_gamma.setObjectName("spinBox_gamma ")
        self.label_subsample = QLabel('subsample')
        self.label_subsample.setEnabled(True)
        self.spinBox_subsample  = QSpinBox()
        self.spinBox_subsample.setEnabled(True)
        self.spinBox_subsample.setPrefix("")
        self.spinBox_subsample.setMinimum(1)
        self.spinBox_subsample.setMaximum(10)
        self.spinBox_subsample.setSingleStep(1)
        self.spinBox_subsample.setProperty("value", 1)
        self.spinBox_subsample.setObjectName("spinBox_subsample ")
        formLayout = QFormLayout()
        formLayout.addRow(self.label_learning_rate,self.spinBox)
        formLayout.addRow(self.label_n_estimators,self.spinBox_n_estimators)
        formLayout.addRow(self.label_max_depth,self.spinBox_max_depth)
        formLayout.addRow(self.label_min_child_weight,self.spinBox_min_child_weight)
        formLayout.addRow(self.label_gamma,self.spinBox_gamma)
        formLayout.addRow(self.label_subsample,self.spinBox_subsample)
        hbox.addLayout(formLayout)
        vbox.addLayout(hbox)
        self.downleft.tab3.setLayout(vbox)
        res={'spinBox':self.spinBox.value(),'spinBox_n_estimators':self.spinBox_n_estimators.value(),'spinBox_max_depth':self.spinBox_max_depth.value(),'spinBox_min_child_weight':self.spinBox_min_child_weight.value(),'spinBox_gamma':self.spinBox_gamma.value(),'spinBox_subsample':self.spinBox_subsample.value()}
        return res
    def fun_Run(self):
        print('进入fun_Run函数')
        if (self.downleft.data_train != None) and (self.downleft.data_val != None) and (len(self.downleft.feature_selected) != 0) and (
                self.downleft.feature_pre != None):
            datafile_train = './data/' + self.downleft.data_train
            datafile_test = './data/' + self.downleft.data_val
            data_test = pd.read_csv(datafile_train)
            info=self.tab3UI()
            # learning_rate = info['spinBox']
            # n_estimators = info['spinBox_n_estimators']
            # max_depth = info['spinBox_max_depth']
            # min_child_weight = info['spinBox_min_child_weight']
            # gamma=info['spinBox_gamma']
            # subsample=info['spinBox_subsample']
            # options = {'learning_rate':learning_rate,
            #     'n_estimators':n_estimators,
            #        'max_depth':max_depth,'min_child_weight':min_child_weight,
            #        'gamma':gamma,
            #        'subsample':subsample
            #            }
            options = {
                       }
            data = XGBoost_test.data_process(datafile_train, datafile_test, self.downleft.feature_selected, self.downleft.feature_pre)
            res = XGBoost_test.train_useXGBoost(data, options)
            self.downright.textLine_acc.setText(str(res['acc']))
            self.downright.textLine_recall.setText(str(res['recall_score']))
            self.downright.textLine_f1.setText(str(res['f1_score']))
            print(str(res['confusion_matrix']))
            Png=QPixmap('XGBoost_Facies_fig_270.png')
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
