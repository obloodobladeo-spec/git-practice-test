import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QPushButton, QLabel,
    QStackedWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedWidget 예제")
        size = self.resize(400, 300)

        # QStackedWidget 생성
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # 페이지 생성
        self.page1 = self.create_menu_page()
        self.page2 = self.create_inventory_page()

        # 페이지 등록
        self.stack.addWidget(self.page1)   # index 0
        self.stack.addWidget(self.page2)   # index 1

    # -------------------------
    # 첫 번째 페이지
    # -------------------------
    def create_menu_page(self):
        page = QWidget()
        layout = QVBoxLayout()

        title = QLabel("메뉴를 선택하세요")

        btn_all = QPushButton("전체 재고")
        btn_americano = QPushButton("아메리카노")

        layout.addWidget(title)
        layout.addWidget(btn_all)
        layout.addWidget(btn_americano)
        layout.addStretch()

        page.setLayout(layout)

        # 버튼을 누르면 2페이지로 이동
        btn_all.clicked.connect(self.show_inventory)
        btn_americano.clicked.connect(self.show_inventory)

        return page

    # -------------------------
    # 두 번째 페이지
    # -------------------------
    def create_inventory_page(self):
        page = QWidget()
        layout = QVBoxLayout()

        self.label = QLabel("재고 화면")

        back_btn = QPushButton("뒤로가기")

        layout.addWidget(self.label)
        layout.addWidget(back_btn)

        page.setLayout(layout)

        back_btn.clicked.connect(self.show_menu)

        return page

    # -------------------------
    # 페이지 전환
    # -------------------------
    def show_inventory(self):
        self.label.setText("재고 목록입니다.")
        self.stack.setCurrentIndex(1)

    def show_menu(self):
        self.stack.setCurrentIndex(0)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())