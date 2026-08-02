import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("menuedit.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.gridLayout.addWidget(QPushButton("(0,0)"), 0,0)
        self.gridLayout.addWidget(QPushButton("(0,1)"), 0,1)
        self.gridLayout.addWidget(QPushButton("(1,0)"), 1,0)
        self.gridLayout.addWidget(QPushButton("(1,1)"), 1,1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()

