import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import structure
import pandas as pd
import RF_test
import matplotlib as mpl  
import matplotlib.pyplot as plt  
import pandas as pd  
class newMainWindow(QWidget):
    def __init__(self):
        super(newMainWindow, self).__init__()
        self.initUI()
        self.setObjectName('RF')

    def initUI(self):
        # self.widget = QWidget()
        self.topleft=structure.topleft()
        self.downleft=structure.downleft()
        #downleft.tab3UI()=tab3UI()
        self.topright=structure.topright()
        self.downright=structure.downright_reg()
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

        #self.downleft = RF_DownLeft.downleft()
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
        print(self.topleft.listwidget_train)
        self.topleft.listwidget_val.clicked.connect(self.downleft_fea)
        self.topleft.listwidget_test.clicked.connect(self.downleft_fea)
        self.downleft.button_Run.clicked.connect(self.fun_Run)

    def downleft_fea(self):
        if self.topleft.tabWidget.currentWidget().objectName() == '训练数据':
            for i in range(self.downleft.layout_tab1_grid.count()):
                self.downleft.layout_tab1_grid.itemAt(i).widget().deleteLater()
           
            datafile = pd.read_csv('./data/' + self.topleft.listwidget_train.currentItem().text())
            print(self.topleft.listwidget_train.currentItem().text())
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
        self.label_n_estimators = QLabel('n_estimators')
        self.label_n_estimators.setEnabled(True)
        self.spinBox = QDoubleSpinBox()
        self.spinBox.setEnabled(True)
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setSingleStep(1)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.label_criterion = QLabel("criterion")
        self.label_criterion.setEnabled(True)
        self.combox_criterion = QComboBox()
        self.combox_criterion.setEnabled(True)
        self.combox_criterion.addItem("")
        self.combox_criterion.addItem("")
        self.combox_criterion.setCurrentText("gini")
        self.combox_criterion.setItemText(0, "gini")
        self.combox_criterion.setItemText(1, "entropy")
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
        formLayout.addRow(self.label_n_estimators,self.spinBox)
        formLayout.addRow(self.label_criterion,self.combox_criterion)
        formLayout.addRow(self.label_gamma,self.combox_gamma)
        formLayout.addRow(self.label_DFS,self.combox_DFS)
        hbox.addLayout(formLayout)
        vbox.addLayout(hbox)
        self.downleft.tab3.setLayout(vbox)
        res={'spinBox':self.spinBox.value(),'combox_criterion':self.combox_criterion.currentText(),'combox_gamma':self.combox_gamma.currentText(),'combox_DFS':self.combox_DFS.currentText()}
        return res
    def fun_Run(self):
        print('进入fun_Run函数')
        if (self.downleft.data_train != None) and (self.downleft.data_val != None) and (len(self.downleft.feature_selected) != 0) and (
                self.downleft.feature_pre != None):
            #print('sssssrrrrrrrrrr'+datafile_train)
            datafile_train = './data/' + self.downleft.data_train
            datafile_test = './data/' + self.downleft.data_val
            data_test = pd.read_csv(datafile_train)
            info=self.tab3UI()
            n_estimators = int(info['spinBox'])
            criterion = info['combox_criterion']
            gamma = info['combox_gamma']
            decision_function_shape = info['combox_DFS']
            options = {'n_estimators': n_estimators,
                       'criterion': criterion,
                       'gamma':gamma,
                       'decision_function_shape':decision_function_shape
                       }
            data = RF_test.data_process(datafile_train, datafile_test, self.downleft.feature_selected, self.downleft.feature_pre)
            res = RF_test.train_useRF(data, options)
            self.showimage_downright(res['path'],self.downleft.feature_pre)
            self.downright.textLine_mse.setText(str(res['mse']))
            self.downright.textLine_mae.setText(str(res['mae']))
            self.downright.textLine_r2.setText(str(res['r2']))
            #self.downright.showWidget.setText(str(res["confusion_matrix"]))
        print('退出fun_run函数')
    def showimage_downright(self,res_path,pre_x):
             # 用Pandas读取csv格式的文件  
        sj = pd.read_csv(res_path)  
         # 提取文件中的数据  
        x = sj['Depth']  
        #BB = sj['Depth']  
        pre = sj[pre_x+'_pre']  
        real = sj[pre_x+'_real']  
        #self.train_data = self.train_data.sort_values(by='Depth')
        # 创建图像  
        fig = plt.figure(figsize=(8,0.8))  #figsize=(10,3)
        # 绘制累计频率曲线  
        plt.plot(x,real,'r--',linewidth = 1,label='real')  
        plt.plot(x,pre,'b-',linewidth = 1,label='pre')  
        # plt.plot(x,MB,':k',linewidth = 1)  
        # 设置题目与坐标轴名称  
        #plt.title('pre and real')  
        plt.ylabel(pre_x)  
        plt.xlabel('Depth') 
        # 设置图例（置于右下方）  
        plt.legend(loc='lower right')  
        # 显示图片  
        #plt.show()
        plt.savefig(pre_x+'_fig.png')
        Png=QPixmap(pre_x+'_fig.png')
        self.downright.showWidget.setPixmap(Png)

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
