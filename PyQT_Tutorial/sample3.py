import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("sample.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.currentTextChanged.connect(self.lineEdit.setText)
        # 함수가 따로 정의 되어 있었음.

    # def changetext(self):
    #     self.lineEdit.setText(self.comboBox.currentText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()

    # combobox.add.items([

    #])

    # self.comboBox.currentTextChanged.connect(self.lineEdit.setText)