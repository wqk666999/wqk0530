import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from welcome import Ui_First
import KNN_ui
import SVC_ui
import kmeans_ui
import gbdt_ui_r
import rf_ui

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout(self)
        self.setWindowTitle('CIFLog')
        self.setWindowIcon(QIcon('./icon.png'))
        self.setGeometry(300, 300, 800, 800)
        bar = self.menuBar()  # 获取菜单栏
        file = bar.addMenu("文件")
        file.addAction("新建")

        save = QAction("保存", self)
        save.setShortcut("Ctrl + S")
        file.addAction(save)

        save.triggered.connect(self.process)

        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("退出", self)
        file.addAction(quit)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(1)

        # 指定列标签
        self.tree.setHeaderLabels([''])

        self.root = QTreeWidgetItem(self.tree)
        self.root.setText(0, '分类')
        # root.setIcon(0, QIcon('./images/root.png'))
        self.tree.setColumnWidth(0, 160)
        # 添加子节点1
        self.child1 = QTreeWidgetItem(self.root)
        self.child1.setText(0, '支持向量机')
        # child1.setText(1, 'DT')
        # child1.setIcon(0, QIcon('./images/bao3.png'))
        # child1.setCheckState(0, Qt.Checked)

        # 添加子节点2
        self.child2 = QTreeWidgetItem(self.root)
        self.child2.setText(0, 'KNN')
        # child2.setIcon(0, QIcon('./images/bao6.png'))
        self.child3 = QTreeWidgetItem(self.root)
        self.child3.setText(0, '梯度提升树')
        self.child4 = QTreeWidgetItem(self.root)
        self.child4.setText(0, '随机森林')


        self.root1 = QTreeWidgetItem(self.tree)
        self.root1.setText(0, '回归')
        # root.setIcon(0, QIcon('./images/root.png'))
        # self.tree.setColumnWidth(0, 160)

        # 为child2添加一个子节点
        self.child5 = QTreeWidgetItem(self.root1)
        self.child5.setText(0, 'GBDT')
        # child3.setText(1, '新的值')
        # child3.setIcon(0, QIcon('./images/music.png')
        
        self.root2 = QTreeWidgetItem(self.tree)
        self.root2.setText(0, '聚类')
        # root.setIcon(0, QIcon('./images/root.png'))
        # self.tree.setColumnWidth(0, 160)
        
        # 为child6添加一个子节点
        self.child6 = QTreeWidgetItem(self.root2)
        self.child6.setText(0, 'K-means')
        # child3.setText(1, '新的值')
        # child3.setIcon(0, QIcon('./images/music.png')

        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.tree)
        # self.splitter1.addWidget(self.topright)
        self.splitter1.setSizes([200])

        self.first = First()
        self.KNN = KNN_ui.KNN_Window()
        self.SVC = SVC_ui.SVC_Window()
        self.RF = rf_ui.rf_Window()
        self.GBDT = gbdt_ui_r.gbdt_Window()
        self.kmeans = kmeans_ui.Kmeans_Window()
        # self.splitter1.addWidget(self.first)
        self.splitter1.addWidget(self.first)

        self.tree.clicked.connect(self.change)
        self.hbox.addWidget(self.splitter1)
        # self.setLayout(self.hbox)
        self.setCentralWidget(self.splitter1)

        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)
    def change(self, index):
        item = self.tree.currentItem().text(0)
        if item == "支持向量机":
            self.splitter1.widget(1).setParent(None)
            self.splitter1.insertWidget(1, self.first)

        if item == "KNN":
            self.splitter1.widget(1).setParent(None)
            self.splitter1.insertWidget(1, self.KNN)
        if item == "支持向量机":
            self.splitter1.widget(1).setParent(None)
            self.splitter1.insertWidget(1, self.SVC)

        if item == '随机森林':
            self.splitter1.widget(1).setParent(None)
            self.splitter1.insertWidget(1,self.RF)

        if item == "GBDT":
            self.splitter1.widget(1).setParent(None)
            self.splitter1.insertWidget(1, self.GBDT)

        if item == 'K-means':
            self.splitter1.widget(1).setParent(None)
            self.splitter1.insertWidget(1,self.kmeans)
    def process(self, a):
        print(self.sender().text())

class First(QWidget, Ui_First):
    def __init__(self):
        super(First, self).__init__()
        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)

        # 设置子窗体最小尺寸
        self.setMinimumWidth(30)
        self.setMinimumHeight(30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainwindow()
    main.show()
    sys.exit(app.exec_())