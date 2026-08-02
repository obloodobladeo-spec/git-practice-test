import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QAbstractItemView,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from db_helper import DB, DB_CONFIG


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = DB(**DB_CONFIG)

        self.setWindowTitle("카페 메뉴 및 재고 관리")
        self.resize(850, 600)

        # 화면 구성
        self.init_ui()

        # 버튼과 함수 연결
        self.connect_signals()

        # 프로그램 실행 시 DB 데이터 조회
        self.load_menu()

    def init_ui(self):
        """
        위젯을 생성하고 화면에 배치하는 함수
        """

        # QMainWindow 중앙에 들어갈 기본 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 전체 화면 세로 레이아웃
        main_layout = QVBoxLayout(central_widget)

        # 제목
        title_label = QLabel("카페 메뉴 관리")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            """
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
            }
            """
        )
        main_layout.addWidget(title_label)

        # 입력 영역 생성
        input_group = self.create_input_group()
        main_layout.addWidget(input_group)

        # 버튼 영역 생성
        button_layout = self.create_button_layout()
        main_layout.addLayout(button_layout)

        # 메뉴 테이블 생성
        self.create_menu_table()
        main_layout.addWidget(self.menu_table)

    def create_input_group(self):
        """
        일련번호, 상품명, 가격, 재고 입력 영역 생성
        """

        group_box = QGroupBox("메뉴 정보")
        form_layout = QFormLayout(group_box)

        # 일련번호
        self.menu_id_edit = QLineEdit()
        self.menu_id_edit.setReadOnly(True)
        self.menu_id_edit.setPlaceholderText("자동 생성")

        # 상품명
        self.product_name_edit = QLineEdit()
        self.product_name_edit.setPlaceholderText("예: 아메리카노")
        self.product_name_edit.setMaxLength(100)

        # 가격
        self.price_spin_box = QSpinBox()
        self.price_spin_box.setRange(0, 10_000_000)
        self.price_spin_box.setSingleStep(500)
        self.price_spin_box.setSuffix(" 원")

        # 재고
        self.stock_spin_box = QSpinBox()
        self.stock_spin_box.setRange(0, 100_000)
        self.stock_spin_box.setSuffix(" 개")

        form_layout.addRow("일련번호:", self.menu_id_edit)
        form_layout.addRow("상품명:", self.product_name_edit)
        form_layout.addRow("가격:", self.price_spin_box)
        form_layout.addRow("재고:", self.stock_spin_box)

        return group_box

    def create_button_layout(self):
        """
        등록, 수정, 삭제, 초기화, 새로고침 버튼 생성
        """

        button_layout = QHBoxLayout()

        self.insert_button = QPushButton("등록")
        self.update_button = QPushButton("수정")
        self.delete_button = QPushButton("삭제")
        self.clear_button = QPushButton("초기화")
        self.refresh_button = QPushButton("새로고침")

        button_layout.addWidget(self.insert_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addStretch()
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.refresh_button)

        return button_layout

    def create_menu_table(self):
        """
        메뉴 목록을 표시할 테이블 생성
        """

        self.menu_table = QTableWidget()

        self.menu_table.setColumnCount(4)
        self.menu_table.setHorizontalHeaderLabels(
            ["일련번호", "상품명", "가격", "재고"]
        )

        # 한 번에 한 행만 선택
        self.menu_table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.menu_table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        # 테이블을 직접 수정하지 못하도록 설정
        self.menu_table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        # 세로 일련번호 숨기기
        self.menu_table.verticalHeader().setVisible(False)

        # 열 크기 설정
        header = self.menu_table.horizontalHeader()
        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents,
        )
        header.setSectionResizeMode(
            1,
            QHeaderView.Stretch,
        )
        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents,
        )
        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents,
        )

    def connect_signals(self):
        """
        버튼이나 테이블 이벤트를 함수와 연결
        """

        self.insert_button.clicked.connect(self.insert_menu)
        self.update_button.clicked.connect(self.update_menu)
        self.delete_button.clicked.connect(self.delete_menu)
        self.clear_button.clicked.connect(self.clear_inputs)
        self.refresh_button.clicked.connect(self.load_menu)

        self.menu_table.cellClicked.connect(
            self.select_menu
        )

    def load_menu(self):
        """
        MySQL의 menu 테이블 데이터를 조회하여
        QTableWidget에 표시
        """

        try:
            menu_list = self.db.get_all_menu()

            self.menu_table.setRowCount(len(menu_list))

            for row, menu in enumerate(menu_list):
                menu_id_item = QTableWidgetItem(
                    str(menu["menu_id"])
                )
                product_name_item = QTableWidgetItem(
                    menu["product_name"]
                )
                price_item = QTableWidgetItem(
                    f'{menu["price"]:,}'
                )
                stock_item = QTableWidgetItem(
                    str(menu["stock"])
                )

                # 숫자 데이터 가운데 정렬
                menu_id_item.setTextAlignment(Qt.AlignCenter)
                price_item.setTextAlignment(Qt.AlignCenter)
                stock_item.setTextAlignment(Qt.AlignCenter)

                self.menu_table.setItem(
                    row,
                    0,
                    menu_id_item,
                )
                self.menu_table.setItem(
                    row,
                    1,
                    product_name_item,
                )
                self.menu_table.setItem(
                    row,
                    2,
                    price_item,
                )
                self.menu_table.setItem(
                    row,
                    3,
                    stock_item,
                )

        except RuntimeError as error:
            QMessageBox.critical(
                self,
                "데이터베이스 오류",
                str(error),
            )

    def insert_menu(self):
        """
        새로운 메뉴 등록
        """

        product_name = self.product_name_edit.text().strip()
        price = self.price_spin_box.value()
        stock = self.stock_spin_box.value()

        if not product_name:
            QMessageBox.warning(
                self,
                "입력 오류",
                "상품명을 입력하세요.",
            )
            self.product_name_edit.setFocus()
            return

        try:
            new_menu_id = self.db.insert_menu(
                product_name,
                price,
                stock,
            )

            QMessageBox.information(
                self,
                "등록 완료",
                f"메뉴가 등록되었습니다.\n일련번호: {new_menu_id}",
            )

            self.clear_inputs()
            self.load_menu()

        except RuntimeError as error:
            QMessageBox.critical(
                self,
                "등록 실패",
                str(error),
            )

    def update_menu(self):
        """
        선택한 메뉴 수정
        """

        menu_id_text = self.menu_id_edit.text().strip()

        if not menu_id_text:
            QMessageBox.warning(
                self,
                "선택 오류",
                "수정할 메뉴를 표에서 선택하세요.",
            )
            return

        product_name = self.product_name_edit.text().strip()
        price = self.price_spin_box.value()
        stock = self.stock_spin_box.value()

        if not product_name:
            QMessageBox.warning(
                self,
                "입력 오류",
                "상품명을 입력하세요.",
            )
            return

        try:
            changed_rows = self.db.update_menu(
                int(menu_id_text),
                product_name,
                price,
                stock,
            )

            if changed_rows == 0:
                QMessageBox.warning(
                    self,
                    "수정 실패",
                    "수정할 메뉴가 없거나 값이 변경되지 않았습니다.",
                )
                return

            QMessageBox.information(
                self,
                "수정 완료",
                "메뉴 정보가 수정되었습니다.",
            )

            self.clear_inputs()
            self.load_menu()

        except RuntimeError as error:
            QMessageBox.critical(
                self,
                "수정 실패",
                str(error),
            )

    def delete_menu(self):
        """
        선택한 메뉴 삭제
        """

        menu_id_text = self.menu_id_edit.text().strip()

        if not menu_id_text:
            QMessageBox.warning(
                self,
                "선택 오류",
                "삭제할 메뉴를 표에서 선택하세요.",
            )
            return

        product_name = self.product_name_edit.text().strip()

        answer = QMessageBox.question(
            self,
            "삭제 확인",
            f"'{product_name}' 메뉴를 삭제하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if answer != QMessageBox.Yes:
            return

        try:
            deleted_rows = self.db.delete_menu(
                int(menu_id_text)
            )

            if deleted_rows == 0:
                QMessageBox.warning(
                    self,
                    "삭제 실패",
                    "삭제할 메뉴를 찾을 수 없습니다.",
                )
                return

            QMessageBox.information(
                self,
                "삭제 완료",
                "메뉴가 삭제되었습니다.",
            )

            self.clear_inputs()
            self.load_menu()

        except RuntimeError as error:
            QMessageBox.critical(
                self,
                "삭제 실패",
                str(error),
            )

    def select_menu(self, row, column):
        """
        테이블에서 선택한 메뉴 정보를 입력창에 표시
        """

        menu_id_item = self.menu_table.item(row, 0)
        product_name_item = self.menu_table.item(row, 1)
        price_item = self.menu_table.item(row, 2)
        stock_item = self.menu_table.item(row, 3)

        if any(
            item is None
            for item in (
                menu_id_item,
                product_name_item,
                price_item,
                stock_item,
            )
        ):
            return

        menu_id = menu_id_item.text()
        product_name = product_name_item.text()

        # "3,000"에서 쉼표 제거 후 정수로 변환
        price = int(price_item.text().replace(",", ""))
        stock = int(stock_item.text())

        self.menu_id_edit.setText(menu_id)
        self.product_name_edit.setText(product_name)
        self.price_spin_box.setValue(price)
        self.stock_spin_box.setValue(stock)

    def clear_inputs(self):
        """
        입력창과 테이블 선택 상태 초기화
        """

        self.menu_id_edit.clear()
        self.product_name_edit.clear()
        self.price_spin_box.setValue(0)
        self.stock_spin_box.setValue(0)

        self.menu_table.clearSelection()
        self.product_name_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())