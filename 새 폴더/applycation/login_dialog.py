# login_dialog.py
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit,\
      QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG
from PyQt5.QtCore import Qt

class LoginDialog(QDialog): # QDialog 클래스(부모클래스)를 상속받음
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("로그인")
        self.db = DB(**DB_CONFIG) # DB클래스를 통한 인스턴스 생성

        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password) # 에코 모드(비밀번호 안보이게 하는거)

        form = QFormLayout()  # 로그인 레이아웃을 추가
        form.addRow("아이디", self.username)  # 레이아웃의 줄을 추가하는 함수 : 아이디, 비밀번호추가
        form.addRow("비밀번호", self.password)

        self.btn_login = QPushButton("로그인")  # 로그인 버튼 추가
        self.btn_login.clicked.connect(self.try_login) # 클릿 했을 때 시그널
        self.btn_login.setDefault(True)

        # 회원가입 버튼 추가
        self.btn_rgt = QPushButton("회원가입")  
        self.btn_rgt.clicked.connect(self.try_register)

        QVlayout = QHBoxLayout() # 수직 레이아웃
        QVlayout.addWidget(self.btn_login) # 로그인 버튼 추가
        QVlayout.addWidget(self.btn_rgt) # 로그인 버튼 추가

        layout = QVBoxLayout() # 수직 레이아웃
        layout.addLayout(form) # 로그인 레이아웃을 추가 
        layout.addLayout(QVlayout) # 로그인 버튼 레이아웃을 추가

        self.setLayout(layout) # 수직 레이아웃을 창에 넣기

    def try_login(self): # 버튼에 넣었던 함수
        uid = self.username.text().strip() # strip() = 앞뒤 공백 제거
        pw = self.password.text().strip()
        if not uid or not pw:   # 아이디, 비번 LINEEDIT가 공백이면 실행되는 값
            QMessageBox.warning(self, "오류", "아이디와 비밀번호를 모두 입력하세요.")
            return

        ok = self.db.verify_user(uid, pw) # 이 기능상 둘다 맞아야 조회가 됨
        if ok: # ok 변수가 True라면 
            self.accept()
        else:  # false면
            QMessageBox.critical(self, "실패", "아이디 또는 비밀번호가 올바르지 않습니다.")

    def try_register(self): # 버튼에 넣었던 함수
        uid = self.username.text().strip() # strip() = 앞뒤 공백 제거
        pw = self.password.text().strip()
        if not uid or not pw:   # 아이디, 비번 LINEEDIT가 공백이면 실행되는 값
            QMessageBox.warning(self, "오류", "아이디와 비밀번호를 모두 입력하세요.")
            return

        ok = self.db.rgt_user(uid, pw) # 이 기능상 둘다 맞아야 조회가 됨
        if ok: # ok 변수가 True라면
            QMessageBox.information(self, "완료", "회원가입이 완료되었습니다.")
            self.username.clear()
            self.password.clear()
        else:  # false면
            QMessageBox.critical(self, "실패", "아이디 또는 비밀번호가 올바르지 않습니다.")