import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets;
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from frontend import Ui_MainWindow
from backend import *

class project_piton_rawr(QDialog):
    def __init__(self):
        super(project_piton_rawr, self).__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())