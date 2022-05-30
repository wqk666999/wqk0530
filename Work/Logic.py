
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from UI import Ui_MainWindow


class LogicWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # logic:逻辑  业务逻辑代码
    def __init__(self):
        self.num = 1
        super(LogicWindow, self).__init__()
        self.setupUi(self,self.num)

    def add(self):
        self.num += 1
        print(self.num)
        self.setupUi(self,self.num)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LogicWindow()
    win.show()
    sys.exit(app.exec_())
