import sys
from PyQt5.QtWidgets import *
from random import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        window = QWidget() # 프레임 안의 위젯
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("버튼 1"))
        layout.addWidget(QPushButton("버튼 2"))
        layout.addWidget(QPushButton("버튼 3"))

        layout2 = QGridLayout()
        layout2.addWidget(QPushButton("(0,0)"), 0,0)
        layout2.addWidget(QPushButton("(0,1)"), 0,1)
        layout2.addWidget(QPushButton("(1,0)"), 1,0)
        layout2.addWidget(QPushButton("(1,1)"), 1,1)

        window.setLayout(layout2) # 정의한 레이아웃을 화면 위젯에 적용하기
        self.setCentralWidget(window) # 정의한 화면을 창에다가 적용하기 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()