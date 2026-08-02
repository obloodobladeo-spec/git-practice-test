import sys
from PyQt5.QtWidgets import QApplication
from login_dialog import LoginDialog
from main import MainWindow

# 개인 묘듈을 사용할 때 필요한 기능
if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginDialog()
    if login.exec_() == LoginDialog.Accepted:
        w = MainWindow()
        w.show()
        sys.exit(app.exec_()) # 창 닫으면 프로그램 종료
    else:
        sys.exit(0)