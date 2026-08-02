import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("sample.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # label 정의
        self.label.setText("버튼의 세계에 온걸 환영한다.")

        # Qtext edit 설정
        self.plainTextEdit.setPlainText("여기에 글을 입력해 보세요!")
        self.btnClear.setEnabled(False)
        self.btnClear.clicked.connect(self.clearText)

        #QPushButton 설정
        self.pushButton.setText("Click Here!")
        self.pushButton.clicked.connect(self.func) # 이벤트 핸들링 

        #QLineEdit 설정
        self.lineEdit.setPlaceholderText("여기에 입력하세요")

    def clearText(self):
        self.plainTextEdit.clear()

    def func(self) :
        self.label.setText("마포대교는 무너졌냐 이새끼야!")
        self.plainTextEdit.setText("어것은 장짜리여")
        self.btnClear.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()