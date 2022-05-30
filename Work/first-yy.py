from PyQt5.QtWidgets import QApplication,QMainWindow,QAction
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
import sys,os,shutil

class Main_Win(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('首页')
        self.resize(900, 800)

        menu = self.menuBar()  # 当前Main_WinM窗体创建menuBar
        file_menu = menu.addMenu('文件')
        edit_menu = menu.addMenu('编辑')
        tool_menu = menu.addMenu('工具')
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

        action_exit = QAction('关闭', self)  # 定义一个Action即动作
        action_exit.setStatusTip('关闭软件')
        action_exit.triggered.connect(self.app.quit)  # 触发事件动作为"关闭窗口"
        action_exit.setShortcut('Ctrl+Q')
        self.statusBar()  # 状态栏信
        file_menu.addAction(action_new)
        file_menu.addAction(action_open)
        file_menu.addAction(action_save)
        file_menu.addAction(action_exit)

        self.outer_win = QWidget()
        self.setCentralWidget(self.outer_win)
        outer_layout = QHBoxLayout()   #全局最外层布局
        outer_layout.setSpacing(0)
        self.outer_win.setLayout(outer_layout)

        #最左边任务栏
        mask_bar = QWidget()
        mask_bar.setObjectName("mask_bar")
        mask_bar.setStyleSheet("#mask_bar{background:rgba(255,255,255)}")
        mask_bar.setStyleSheet("#mask_bar{border:1px solid black}")
        mask_bar.setFixedWidth(30)
        mask_btn = QtWidgets.QPushButton(mask_bar)
        mask_btn.setText("任\n务\n栏")
        mask_btn.setFixedWidth(30)
        mask_btn.setFixedHeight(80)
        mask_btn.clicked.connect(self.mask_visible)

        #主窗口
        main = self.hello_page()
        main.setObjectName("main")
        #main.setStyleSheet("#main{border:0px solid black}")

        #任务栏窗口   （作为主窗口的 子窗口）
        outer_main_layout = QHBoxLayout()
        self.mask_win = QTabWidget()
        self.mask_win.setFixedWidth(300)
        self.mask_win.setMinimumHeight(700)
        # self.mask_win.resize(200,1000)

        self.mask_win_visible = False
        self.mask_win.setVisible(self.mask_win_visible)
        self.mask_win.setObjectName("mask_win")
        self.mask_win.setStyleSheet("#mask_win{border:1px solid black}")
        #选项卡
        self.tab1 = QWidget()  #分类
        self.tab2 = QWidget()  #回归
        self.tab3 = QWidget()  #聚类
        self.tab4 = QWidget()  #综合分析
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

        self.mask_win.addTab(self.tab1, '分类')
        self.mask_win.addTab(self.tab2, '回归')
        self.mask_win.addTab(self.tab3, '聚类')
        self.mask_win.addTab(self.tab4, '综合分析')
        self.mask_win.setTabPosition(QTabWidget.South)

        main.setLayout(outer_main_layout)
        outer_main_layout.addChildWidget(self.mask_win)
        outer_layout.addWidget(mask_bar)
        outer_layout.addWidget(main)


    def file_open_action(self):
        files,_ = QFileDialog.getOpenFileNames(self,"选取文件",os.getcwd())
        print(files)
        for i in range(len(files)):
            _, filename = os.path.split(files[i])
            newfile = '../data/'+ filename
            shutil.copyfile(files[i],newfile)

    def file_new_action(self):
        pass

    def mask_visible(self):
        self.mask_win_visible = not self.mask_win_visible
        self.mask_win.setVisible(self.mask_win_visible)


    def tab1UI(self):
        layout1 = QVBoxLayout()
        self.tab1.setLayout(layout1)
        layout2 = QHBoxLayout()
        btn_SVM = QPushButton('SVM')
        btn_SVM.setFixedHeight(120)
        #btn_SVM.setGeometry(QtCore.QRect(50,50,300,300))
        btn_RF = QPushButton('RF')
        btn_RF.setFixedHeight(120)
        btn_GBDT = QPushButton('GBDT')
        btn_GBDT.setFixedHeight(120)
        layout2.addWidget(btn_SVM)
        layout2.addWidget(btn_RF)
        layout2.addWidget(btn_GBDT)
        layout1.addLayout(layout2)


    def tab2UI(self):
        layout1 = QVBoxLayout()
        self.tab2.setLayout(layout1)
        layout2 = QHBoxLayout()
        btn_SVM = QPushButton('SVM')
        btn_SVM.setFixedHeight(120)
        btn_RF = QPushButton('RF')
        btn_RF.setFixedHeight(120)
        btn_GBDT = QPushButton('GBDT')
        btn_GBDT.setFixedHeight(120)
        layout2.addWidget(btn_SVM)
        layout2.addWidget(btn_RF)
        layout2.addWidget(btn_GBDT)
        layout1.addLayout(layout2)

    def tab3UI(self):
        layout1 = QVBoxLayout()
        self.tab3.setLayout(layout1)
        layout2 = QHBoxLayout()
        btn_kmeans = QPushButton('K-Means')
        btn_kmeans.setFixedHeight(120)
        btn_kmeans.setFixedWidth(90)
        layout2.addWidget(btn_kmeans)
        layout1.addLayout(layout2)

    def tab4UI(self):
        pass

    def hello_page(self):
        h = QWidget()
        # page_layout = QHBoxLayout()
        # h.setLayout(page_layout)
        # label = QLabel()
        # page_layout.addWidget(label)
        label = QtWidgets.QLabel(h)
        label.setGeometry(QtCore.QRect(190, 300, 431, 201))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(60)
        label.setFont(font)
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText("欢迎使用")
        return h


if __name__=='__main__':
    Main_Win = Main_Win()
    Main_Win.show()
    sys.exit(Main_Win.app.exec())