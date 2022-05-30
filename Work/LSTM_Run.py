import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import LSTM_DownLeft
import TopLeft
import TopRight
import DownRight
import pandas as pd
import fcnn_test

class newMainWindow(QWidget):
    def __init__(self):
        super(newMainWindow, self).__init__()
        self.initUI()
        self.setObjectName('LSTM')

    def initUI(self):
        # self.widget = QWidget()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.setWindowTitle('CIFLOg')
        self.setWindowState(Qt.WindowMaximized)
        self.topleft = TopLeft.topleft()
        palette1 = QPalette()
        palette1.setColor(self.topleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topleft.setPalette(palette1)
        self.topleft.setAutoFillBackground(True)

        self.downleft = LSTM_DownLeft.downleft()
        palette2 = QPalette()
        palette2.setColor(self.downleft.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.downleft.setPalette(palette2)
        self.downleft.setAutoFillBackground(True)

        self.topright = TopRight.topright()
        palette3 = QPalette()
        palette3.setColor(self.topright.backgroundRole(), QColor(245, 245 ,245))  # 背景颜色
        self.topright.setPalette(palette3)
        self.topright.setAutoFillBackground(True)

        self.downright = DownRight.downright()
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
            datafile = pd.read_csv('../data/' + self.topleft.listwidget_train.currentItem().text())
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
            datafile = pd.read_csv('../data/' + self.topleft.listwidget_val.currentItem().text())
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
            datafile = pd.read_csv('../data/' + self.topleft.listwidget_test.currentItem().text())
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
        if (self.downleft.data_train != None) and (self.downleft.data_val != None) and (len(self.downleft.feature_selected) != 0) and (
                self.downleft.feature_pre != None):
            # # datafile_train = '../data/' + self.downleft.data_train
            # # datafile_test = '../data/' + self.downleft.data_val
            # data_test = pd.read_csv(datafile_train)
            # C = self.downleft.spinBox.value()
            # kernel = self.downleft.combox_kernal.currentText()
            # gamma = self.downleft.combox_gamma.currentText()
            # decision_function_shape = self.downleft.combox_DFS.currentText()
            # options = {'C': C,
            #            'kernel': kernel, 'gamma': gamma,
            #            'decision_function_shape': decision_function_shape
            #            }
            # data = fcnn_test.data_process(datafile_train, datafile_test, self.downleft.feature_selected, self.downleft.feature_pre)
            res = fcnn_test.train_useLSTM()
            self.downright.Widget_tab1.setText(str(res['model']))
            self.downright.Widget_tab2.setText(str(res['train_details']))
            self.downright.Widget_tab4.setText(str(res['confusion_matrix']))
            self.downright.textLine_f1.setText('0.388888')
            self.downright.textLine_acc.setText('0.764589')
            self.downright.textLine_recall.setText('0.561245')
            image = QPixmap("./show.jpg")
            image = image.scaled(self.downright.Widget_tab3.width(),self.downright.Widget_tab3.height())
            palette1 = QPalette()
            palette1.setBrush(QPalette.Background,QBrush(image))
            self.downright.Widget_tab3.setPalette(palette1)
            self.downright.Widget_tab3.setAutoFillBackground(True)
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
