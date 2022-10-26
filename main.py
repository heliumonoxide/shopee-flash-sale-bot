import sys
from PyQt5.uic import loadUI
from PyQt5 import QtWidgets;
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

class project_piton_rawr(QDialog):
    def __init__(self):
        super(project_piton_rawr, self).__init__()
        loadUi("project_piton_rawr.ui", self)


# main
app = QApplication(sys.argv)
welcome=project_piton_rawr()
