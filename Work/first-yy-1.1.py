import os
import shutil
import sys
import SVC_Run
import RF_Run
import KNN_Run
import GBDTR_Run
import LSTM_Run
import XGBoost_Run
import yDCNN_BiLSTM_Run
import LI_GCN_Run
import kmeans_ui
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QAction


class Main_Win(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('首页')
        self.resize(900, 800)

        #主窗口添加菜单部分
        menu = self.menuBar()  # 当前Main_WinM窗体创建menuBar
        file_menu = menu.addMenu('文件')
        edit_menu = menu.addMenu('编辑')
        tool_menu = menu.addMenu('工具')
        window_menu = menu.addMenu('窗口')
        help_menu = menu.addMenu('帮助')

        action_new = QAction('新建',self)
        action_new.setStatusTip('新建项目')  # 状态栏信息
        action_new.setShortcut('Ctrl+N')  # 快捷键设置
        action_new.triggered.connect(self.file_new_action)   #新建项目
        action_open = QAction('打开',self)
        action_open.setStatusTip('打开项目目录')
        action_open.setShortcut('Ctrl+O')
        action_open.triggered.connect(self.file_open_action)
        action_save = QAction('另存为',self)
        action_save.setStatusTip('另存为')
        action_exit = QAction('关闭', self)
        action_exit.setStatusTip('关闭软件')
        action_exit.triggered.connect(self.app.quit)  # 触发事件动作为"关闭窗口"
        action_exit.setShortcut('Ctrl+Q')
        action_maskwin = QAction('任务栏',self)
        action_maskwin.setStatusTip('打开任务栏')
        action_maskwin.triggered.connect(self.mask_win)

        self.statusBar()  # 状态栏信
        file_menu.addAction(action_new)
        file_menu.addAction(action_open)
        file_menu.addAction(action_save)
        file_menu.addAction(action_exit)
        window_menu.addAction(action_maskwin)


        #最左边任务栏
        # mask_bar = QWidget()
        # mask_bar.setObjectName("mask_bar")
        # mask_bar.setStyleSheet("#mask_bar{background:rgba(255,255,255)}")
        # mask_bar.setStyleSheet("#mask_bar{border:1px solid black}")
        # mask_bar.setFixedWidth(30)
        # mask_btn = QtWidgets.QPushButton(mask_bar)
        # mask_btn.setText("任\n务\n栏")
        # mask_btn.setFixedWidth(30)
        # mask_btn.setFixedHeight(80)
        # mask_btn.clicked.connect(self.mask_visible)


        #主窗口
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        self.main_page = QTabWidget()
        self.main_page.setTabsClosable(True)    #tab中删除图标 可见
        self.main_page.tabCloseRequested.connect(self.tabclose)   #tab关闭的 点击信号
        self.hello_tab = self.hello_page()
        self.setCentralWidget(self.main_page)
        self.main_page.addTab(self.hello_tab, '欢迎页')
        self.exist_maskwin = False  #判断任务栏是否存在


    #任务栏 （使用停靠窗口）
    def mask_win(self):
        if self.exist_maskwin == False:
            self.maskWin = QDockWidget("任务栏", self)
            self.mask_win = QTabWidget()
            # 选项卡
            self.tab1 = QWidget()  # 分类
            self.tab2 = QWidget()  # 回归
            self.tab3 = QWidget()  # 聚类
            self.tab4 = QWidget()  # 综合分析
            self.tab1UI()
            self.tab2UI()
            self.tab3UI()
            self.tab4UI()

            self.mask_win.addTab(self.tab1, '分类')
            self.mask_win.addTab(self.tab2, '回归')
            self.mask_win.addTab(self.tab3, '聚类')
            self.mask_win.addTab(self.tab4, '综合分析')
            self.mask_win.setTabPosition(QTabWidget.South)
            self.maskWin.setWidget(self.mask_win)
            self.exist_maskwin = True
            #将任务栏加入主窗口
            self.addDockWidget(Qt.LeftDockWidgetArea,self.maskWin)
        else:
            self.maskWin.setVisible(True)


    #tab 删除的实现
    def tabclose(self,index):
        self.main_page.setTabVisible(index,False)
        #self.main_page.tabBar().removeTab(index)

    def file_open_action(self):
        files,_ = QFileDialog.getOpenFileNames(self,"选取文件",os.getcwd())
        print(files)
        for i in range(len(files)):
            _, filename = os.path.split(files[i])
            newfile = '../data/'+ filename
            shutil.copyfile(files[i],newfile)

    def file_new_action(self):
        pass

    def tab1UI(self):
        layout1 = QGridLayout()
        self.tab1.setLayout(layout1)
        btn_SVM = QPushButton('SVM(支持向量机)')
        btn_SVM.setFixedHeight(90)
        btn_SVM.clicked.connect(lambda:self.Add_Page(SVC_Run.newMainWindow()))
        btn_RF = QPushButton('GBDT(梯度提升树)')
        btn_RF.setFixedHeight(90)
        btn_RF.clicked.connect(lambda :self.Add_Page(GBDTR_Run.newMainWindow()))
        btn_KNN = QPushButton('KNN(K近邻)')
        btn_KNN.setFixedHeight(90)
        btn_KNN.clicked.connect(lambda :self.Add_Page(KNN_Run.newMainWindow()))
        btn_XGBoost = QPushButton('XGBoost')
        btn_XGBoost.setFixedHeight(90)
        btn_XGBoost.clicked.connect(lambda :self.Add_Page(XGBoost_Run.newMainWindow()))
        btn_1DCNN_BiLSTM = QPushButton('1DCNN-BiLSTM')
        btn_1DCNN_BiLSTM.setFixedHeight(90)
        btn_1DCNN_BiLSTM.clicked.connect(lambda :self.Add_Page(yDCNN_BiLSTM_Run.newMainWindow()))
        btn_Li_STGCN = QPushButton('LI-STGCN')
        btn_Li_STGCN.setFixedHeight(90)
        btn_Li_STGCN.clicked.connect(lambda :self.Add_Page(LI_GCN_Run.newMainWindow()))
        layout1.addWidget(btn_SVM,0,0)
        layout1.addWidget(btn_RF,0,1)
        layout1.addWidget(btn_KNN,1,0)
        layout1.addWidget(btn_XGBoost,1,1)
        layout1.addWidget(btn_1DCNN_BiLSTM,2,0)
        layout1.addWidget(btn_Li_STGCN,2,1)


    def tab2UI(self):
        layout1 = QGridLayout()
        self.tab2.setLayout(layout1)
        btn_SVM = QPushButton('LR(逻辑回归)')
        btn_SVM.setFixedHeight(60)
        btn_SVM.clicked.connect(lambda: self.Add_Page(SVC_Run.newMainWindow()))
        btn_RF = QPushButton('RF(随机森林回归)')
        btn_RF.setFixedHeight(60)
        btn_RF.clicked.connect(lambda: self.Add_Page(RF_Run.newMainWindow()))
        btn_GBDT = QPushButton('GBDT(梯度提升树回归)')
        btn_GBDT.setFixedHeight(60)
        btn_GBDT.clicked.connect(lambda :self.Add_Page(GBDTR_Run.newMainWindow()))
        layout1.addWidget(btn_SVM, 0, 0)
        layout1.addWidget(btn_RF, 0, 1)
        layout1.addWidget(btn_GBDT, 0, 2)

    def tab3UI(self):
        layout1 = QGridLayout()
        self.tab3.setLayout(layout1)
        btn_kmeans = QPushButton('K-Means(K均值聚类)')
        btn_kmeans.setFixedHeight(60)
        btn_kmeans.clicked.connect(lambda: self.Add_Page(kmeans_ui.Kmeans_Window()))
        layout1.addWidget(btn_kmeans,0,0)

    def tab4UI(self):
        layout1 = QGridLayout()
        self.tab4.setLayout(layout1)
        btn_dnn = QPushButton('DNN')
        btn_dnn.setFixedHeight(60)
        #btn_dnn.clicked.connect(lambda: self.Add_Page(GBDTR_Run.newMainWindow()))
        btn_lstm = QPushButton('LSTM')
        btn_lstm.setFixedHeight(60)
        btn_lstm.clicked.connect(lambda: self.Add_Page(LSTM_Run.newMainWindow()))
        btn_cnn = QPushButton('1D-CNN')
        btn_cnn.setFixedHeight(60)
        #btn_cnn.clicked.connect(lambda: self.Add_Page(GBDTR_Run.newMainWindow()))
        layout1.addWidget(btn_dnn, 0, 0)
        layout1.addWidget(btn_lstm, 0, 1)
        layout1.addWidget(btn_cnn, 0, 2)

    def hello_page(self):
        h = QWidget()
        page_layout = QHBoxLayout()
        h.setLayout(page_layout)
        label = QLabel()
        page_layout.addWidget(label)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(60)
        label.setFont(font)
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText("欢迎使用")
        return h

    def Add_Page(self,new_page=None):
        page_name = new_page.objectName()
        self.main_page.addTab(new_page, page_name)
        index = self.main_page.indexOf(new_page)
        # print(index)
        self.main_page.setCurrentIndex(index)
        #print(self.main_page.currentWidget())



if __name__=='__main__':
    Main_Win = Main_Win()
    Main_Win.show()
    sys.exit(Main_Win.app.exec())