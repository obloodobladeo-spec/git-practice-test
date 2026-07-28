import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
import time

form_class = uic.loadUiType("label.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.horizontalSlider.valueChanged.connect(self.change_color)

    def changetext(self):
        self.pushButton_1.setText("이걸 누르네")

    def changetext2(self):
        self.pushButton_1.setText("일단 눌러")

    def change_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.textEdit.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()
