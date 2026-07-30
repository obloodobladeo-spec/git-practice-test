import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG
from PyQt5.QtCore import Qt

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle("로그인")
        self.db = DB(**DB_CONFIG)

        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        form = QFormLayout()
        form.addRow("아이디", self.username)
        form.addRow("비밀번호", self.password)

        # 로그인 버튼 추가
        self.btn_login = QPushButton("로그인") 
        self.btn_login.clicked.connect(self.try_login) # 클릿 했을 때 시그널
        self.btn_login.setDefault(True)

        # 회원가입 버튼 추가
        self.btn_rgt = QPushButton("취소")
        self.btn_rgt.clicked.connect(self.try_exit)

        QVlayout = QHBoxLayout() # 수직 레이아웃
        QVlayout.addWidget(self.btn_login) # 로그인 버튼 추가
        QVlayout.addWidget(self.btn_rgt) # 로그인 버튼 추가

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(QVlayout)

        self.setLayout(layout)

    def try_login(self):
        uid = self.username.text().strip()
        pw = self.password.text().strip()
        if not uid or not pw:
            QMessageBox.warning(self, "오류", "아이디와 비밀번호를 모두 입력하세요.")
            return

        ok = self.db.verify_user(uid, pw)
        if ok:
            self.accept()
        else:
            QMessageBox.critical(self, "실패", "아이디 또는 비밀번호가 올바르지 않습니다.")

    def try_exit(self): # 버튼에 넣었던 함수
        self.reject()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginDialog()
    login.exec_()
    app.exec_() # 창 닫으면 프로그램 종료