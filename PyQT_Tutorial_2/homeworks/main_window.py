# main_window.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, \
    QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QApplication
from PyQt5.QtCore import Qt
from db_helper import DB, DB_CONFIG
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("회원 관리")
        self.db = DB(**DB_CONFIG)

        # 중앙 위젯 및 레이아웃
        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        # 제목
        title = QLabel("카페 제고 관리 시스템")
        title.setAlignment(Qt.AlignCenter) # 중앙 배치

        # 상단: 입력 폼 + 추가 버튼 + 검색 기능
        form_box = QHBoxLayout()
        self.input_name = QLineEdit()
        self.input_email = QLineEdit()
        self.btn_add = QPushButton("추가")
        self.btn_add.clicked.connect(self.add_member)

        # 검색 기능 만들기

        form_box.addWidget(QLabel("이름"))
        form_box.addWidget(self.input_name)
        form_box.addWidget(QLabel("이메일"))
        form_box.addWidget(self.input_email)
        form_box.addWidget(self.btn_add)

        # 중앙: 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["이름", "재고", "단위", "가격"])
        self.table.setEditTriggers(self.table.NoEditTriggers)  # 표준 예시: 목록은 읽기 전용
        self.table.verticalHeader().setVisible(False)


        # bottom_box = QHBoxLayout()
        # self.btn_del = QPushButton("제거")
        # self.btn_del.clicked.connect(self.del_member)

        # bottom_box.addStretch()          # 왼쪽 공간을 모두 차지
        # bottom_box.addWidget(self.btn_del)
    

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
            # 체크박스를 가운데 정렬
            # self.checkbox = QCheckBox()
            # self.cell_widget = QWidget()
            # layout = QHBoxLayout(self.cell_widget)
            # layout.addWidget(self.checkbox)
            # layout.setAlignment(Qt.AlignCenter)
            # layout.setContentsMargins(0, 0, 0, 0)
            # self.table.setCellWidget(r, 3, self.cell_widget)
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

    # def del_member(self):
    #     selected_ids = []

    #     for row in range(self.table.rowCount()):
    #         cell_widget = self.table.cellWidget(row, 3)

    #         if cell_widget is not None:
    #             checkbox = cell_widget.findChild(QCheckBox)

    #             if checkbox is not None and checkbox.isChecked():
    #                 member_id = int(self.table.item(row, 0).text())
    #                 selected_ids.append(member_id)

    #     if not selected_ids:
    #         QMessageBox.warning(self, "오류", "선택된 회원이 없습니다.")
    #         return
    
    #     ok = self.db.delete_member(tuple(selected_ids))
    #     if ok:
    #         QMessageBox.information(self, "완료", "제거되었습니다.")
    #         self.input_name.clear()
    #         self.input_email.clear()
    #         self.load_members()
    #     else:
    #         QMessageBox.critical(self, "에러", "제거 중 오류가 발생했습니다.")
