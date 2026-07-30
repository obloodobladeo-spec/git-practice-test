from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

form_class = uic.loadUiType("sel_menu.ui")[0]

class Sel_Menu(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Sel_Menu()
    window.show()

    app.exec_()