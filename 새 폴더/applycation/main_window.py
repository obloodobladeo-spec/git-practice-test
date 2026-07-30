# main_window.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, \
    QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QApplication, QFormLayout, QSpinBox
from PyQt5.QtCore import Qt
from db_helper import DB, DB_CONFIG
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("회원 관리")
        self.resize(850, 600)
        self.db = DB(**DB_CONFIG)

        # 중앙 위젯 및 레이아웃
        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        # 제목
        title = QLabel("카페 제고 관리 시스템")
        title.setAlignment(Qt.AlignCenter) # 중앙 배치

        # 상단: 입력 폼 + 추가 버튼 + 검색 기능
        form_box = QFormLayout()
        self.input_name = QLineEdit()
        self.input_email = QLineEdit()
        self.input_num = QSpinBox()
        self.input_price = QSpinBox()
        self.btn_add = QPushButton("추가")
        self.btn_add.clicked.connect(self.add_member)

        # 검색 기능 만들기

        form_box.addRow("{0:0>6}".format("이름 : "), self.input_name)
        form_box.addRow("이메일 : ", self.input_email)
        form_box.addRow(self.input_num)
        form_box.addRow(self.input_price)
        form_box.addRow(self.btn_add)

        # 중앙: 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["이름", "재고", "단위", "가격"])
        self.table.setEditTriggers(self.table.NoEditTriggers)  # 표준 예시: 목록은 읽기 전용
        self.table.verticalHeader().setVisible(False)


        # 배치
        vbox.addWidget(title)
        vbox.addLayout(form_box)
        vbox.addWidget(self.table)
        # vbox.addLayout(bottom_box)

        # 초기 데이터 로드
        self.load_members()

    def load_members(self):
        rows = self.db.fetch_members()
        self.table.setRowCount(len(rows))
        for r, (name, stock, unit, price) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(str(stock)))
            self.table.setItem(r, 2, QTableWidgetItem(unit))
            self.table.setItem(r, 3, QTableWidgetItem(str(price)))

        self.table.resizeColumnsToContents()

    def add_member(self):
        name = self.input_name.text().strip()
        email = self.input_email.text().strip()
        if not name or not email:
            QMessageBox.warning(self, "오류", "이름과 이메일을 모두 입력하세요.")
            return
        ok = self.db.insert_member(name, email)
        if ok:
            QMessageBox.information(self, "완료", "추가되었습니다.")
            self.input_name.clear()
            self.input_email.clear()
            self.load_members()
        else:
            QMessageBox.critical(self, "실패", "추가 중 오류가 발생했습니다.")


app = QApplication(sys.argv)

mwindow = MainWindow()
mwindow.show()

sys.exit(app.exec_())