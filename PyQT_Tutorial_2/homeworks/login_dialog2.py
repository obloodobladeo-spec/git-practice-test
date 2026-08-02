import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cafe_manager_project.db_helper import DB, DB_CONFIG

#UI파일 연결
form_class = uic.loadUiType("sample.ui")[0]

#화면을 띄우는데 사용되는 클래스 선언
class Window(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("로그인")
        self.db = DB(**DB_CONFIG)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print("창을 닫을 수 없음") 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("회원 관리")
        self.db = DB(**DB_CONFIG)

        # 중앙 위젯 및 레이아웃
        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        # 상단: 입력 폼 + 추가 버튼 + 검색 기능
        form_box = QHBoxLayout()
        self.input_name = QLineEdit()
        self.input_email = QLineEdit()
        self.btn_add = QPushButton("추가")

        # 검색 기능 만들기

        form_box.addWidget(QLabel("이름"))
        form_box.addWidget(self.input_name)
        form_box.addWidget(QLabel("이메일"))
        form_box.addWidget(self.input_email)
        form_box.addWidget(self.btn_add)

        # 중앙: 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "이름", "이메일", "선택"])
        self.table.setEditTriggers(self.table.NoEditTriggers)  # 표준 예시: 목록은 읽기 전용
        self.table.verticalHeader().setVisible(False)

        bottom_box = QHBoxLayout()
        self.btn_del = QPushButton("제거")

        bottom_box.addStretch()          # 왼쪽 공간을 모두 차지
        bottom_box.addWidget(self.btn_del)
    

        # 배치
        vbox.addLayout(form_box)
        vbox.addWidget(self.table)
        vbox.addLayout(bottom_box)

        # 초기 데이터 로드
        self.load_members()

    def load_members(self):
        rows = self.db.fetch_members()
        self.table.setRowCount(len(rows))
        for r, (mid, name, email) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(str(mid)))
            self.table.setItem(r, 1, QTableWidgetItem(name))
            self.table.setItem(r, 2, QTableWidgetItem(email))
            # 체크박스를 가운데 정렬
            self.checkbox = QCheckBox()
            self.cell_widget = QWidget()
            layout = QHBoxLayout(self.cell_widget)
            layout.addWidget(self.checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(r, 3, self.cell_widget)
        self.table.resizeColumnsToContents()


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = Window()
    myWindow.exec_()

    w = MainWindow()
    w.show()

    app.exec_()