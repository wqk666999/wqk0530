from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class topleft(QWidget):

    def __init__(self):
        super(topleft, self).__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.tabWidget = QTabWidget()
        self.btu1 = QPushButton('增加')
        self.btu2 = QPushButton('删除')
        self.tab1 = QWidget()
        self.tab1.setObjectName('训练数据')
        self.tab2 = QWidget()
        self.tab2.setObjectName('验证数据')
        self.tab3 = QWidget()
        self.tab3.setObjectName('测试数据')
        self.tabWidget.addTab(self.tab1,'训练数据')
        self.tabWidget.addTab(self.tab2,'验证数据')
        self.tabWidget.addTab(self.tab3,'测试数据')
        self.hbox1.addStretch(0)
        self.hbox1.addWidget(self.btu1)
        self.hbox1.addWidget(self.btu2)
        self.hbox1.addStretch(1)
        self.hbox.addWidget(self.tabWidget)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.setLayout(self.vbox)
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255, 255, 255))  # 背景颜色
        self.setPalette(palette1)
        self.btu1.clicked.connect(self.clicked_btu1)
        self.btu2.clicked.connect(self.clicked_btu2)
        self.setAutoFillBackground(True)
    def clicked_btu1(self):
        self.Treeviewwidget = QWidget()
        self.Treeviewwidget.resize(500,500)
        self.Treeviewwidget.setWindowTitle('数据资源')
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()
        self.model = QDirModel()
        self.tree = QTreeView()
        self.btu = QPushButton('确定')
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index('../data'))
        hbox1.addWidget(self.tree)
        hbox2.addStretch(0)
        hbox2.addWidget(self.btu)
        hbox2.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.tree.clicked.connect(self.tree_clicked)
        self.btu.clicked.connect(self.clicked_btn)
        self.Treeviewwidget.setLayout(vbox)
        self.Treeviewwidget.show()
    def clicked_btu2(self):
        if self.tabWidget.currentWidget().objectName() == '训练数据':
            row = self.listwidget_train.currentRow()
            self.listwidget_train.takeItem(row)
        if self.tabWidget.currentWidget().objectName() == '验证数据':
            row = self.listwidget_val.currentRow()
            self.listwidget_val.takeItem(row)
        if self.tabWidget.currentWidget().objectName() == '测试数据':
            row = self.listwidget_test.currentRow()
            self.listwidget_test.takeItem(row)
        QApplication.processEvents()
    def tree_clicked(self,Qmodelidx):
        self.filePath = self.model.filePath(Qmodelidx)
        self.fileName = self.model.fileName(Qmodelidx)
        self.fileInfo = self.model.fileInfo(Qmodelidx)
    def clicked_btn(self):
        if self.tabWidget.currentWidget().objectName() == '训练数据':
            self.listwidget_train.addItem(self.fileName)
        if self.tabWidget.currentWidget().objectName() == '验证数据':
            self.listwidget_val.addItem(self.fileName)
        if self.tabWidget.currentWidget().objectName() == '测试数据':
            self.listwidget_test.addItem(self.fileName)
        QApplication.processEvents()
    def tab1UI(self):
        layout = QHBoxLayout()
        self.listwidget_train = QListWidget()
        layout.addWidget(self.listwidget_train)
        self.tab1.setLayout(layout)
    def tab2UI(self):
        layout = QHBoxLayout()
        self.listwidget_val = QListWidget()
        layout.addWidget(self.listwidget_val)
        self.tab2.setLayout(layout)
    def tab3UI(self):
        layout = QHBoxLayout()
        self.listwidget_test = QListWidget()
        layout.addWidget(self.listwidget_test)
        self.tab3.setLayout(layout)


