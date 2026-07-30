# PyQT로 만든 UI창을 파이선으로 실행하는 코드

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic # ui파일 읽어 드리기

#UI파일 연결
form_class = uic.loadUiType("sample.ui")[0]
# uic.loadUiType("sample.ui") => 리터러블한 값이 나옴 index값 적용

#화면을 띄우는데 사용되는 클래스 선언
class Window(QMainWindow, form_class) : # Qmainwindow QT에서 제공하는 창
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) # QApplication QT창이 정상적으로 돌아가게 해주는 운영체제

    #WindowClass의 인스턴스 생성
    myWindow = Window() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()