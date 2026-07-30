import sys
from datetime import date

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QAbstractItemView,
    QDateEdit,
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

        self.setWindowTitle("카페 메뉴 및 일자별 판매량 관리")
        self.resize(950, 650)

        self.init_ui()
        self.connect_signals()
        self.load_sales()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        title_label = QLabel("카페 일자별 판매량 관리")
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

        # 메뉴 정보를 수평으로 배치
        main_layout.addWidget(self.create_input_group())
        main_layout.addLayout(self.create_button_layout())

        self.create_sales_table()
        main_layout.addWidget(self.sales_table)

    def create_input_group(self):
        group_box = QGroupBox("판매 정보")
        layout = QHBoxLayout(group_box)

        self.sale_id_edit = QLineEdit()
        self.sale_id_edit.setReadOnly(True)
        self.sale_id_edit.setPlaceholderText("자동 생성")
        self.sale_id_edit.setFixedWidth(90)

        self.sale_date_edit = QDateEdit()
        self.sale_date_edit.setCalendarPopup(True)
        self.sale_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.sale_date_edit.setDate(QDate.currentDate())
        self.sale_date_edit.setFixedWidth(130)

        self.product_name_edit = QLineEdit()
        self.product_name_edit.setPlaceholderText("예: 아메리카노")
        self.product_name_edit.setMaxLength(100)

        self.price_spin_box = QSpinBox()
        self.price_spin_box.setRange(0, 10_000_000)
        self.price_spin_box.setSingleStep(500)
        self.price_spin_box.setSuffix(" 원")
        self.price_spin_box.setFixedWidth(140)

        self.sales_quantity_spin_box = QSpinBox()
        self.sales_quantity_spin_box.setRange(0, 100_000)
        self.sales_quantity_spin_box.setSuffix(" 잔")
        self.sales_quantity_spin_box.setFixedWidth(120)

        layout.addWidget(QLabel("번호"))
        layout.addWidget(self.sale_id_edit)
        layout.addWidget(QLabel("날짜"))
        layout.addWidget(self.sale_date_edit)
        layout.addWidget(QLabel("상품명"))
        layout.addWidget(self.product_name_edit, 1)
        layout.addWidget(QLabel("가격"))
        layout.addWidget(self.price_spin_box)
        layout.addWidget(QLabel("판매량"))
        layout.addWidget(self.sales_quantity_spin_box)

        return group_box

    def create_button_layout(self):
        layout = QHBoxLayout()

        self.insert_button = QPushButton("등록")
        self.update_button = QPushButton("수정")
        self.delete_button = QPushButton("삭제")
        self.clear_button = QPushButton("초기화")
        self.refresh_button = QPushButton("새로고침")

        layout.addWidget(self.insert_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)
        layout.addStretch()
        layout.addWidget(self.clear_button)
        layout.addWidget(self.refresh_button)

        return layout

    def create_sales_table(self):
        self.sales_table = QTableWidget()
        self.sales_table.setColumnCount(6)
        self.sales_table.setHorizontalHeaderLabels(
            ["번호", "날짜", "상품명", "가격", "판매량", "매출액"]
        )

        self.sales_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sales_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.sales_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sales_table.verticalHeader().setVisible(False)

        header = self.sales_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)

    def connect_signals(self):
        self.insert_button.clicked.connect(self.insert_sale)
        self.update_button.clicked.connect(self.update_sale)
        self.delete_button.clicked.connect(self.delete_sale)
        self.clear_button.clicked.connect(self.clear_inputs)
        self.refresh_button.clicked.connect(self.load_sales)

        self.sales_table.cellClicked.connect(self.select_sale)

    def load_sales(self):
        try:
            sales_list = self.db.get_all_sales()
            self.sales_table.setRowCount(len(sales_list))

            for row, sale in enumerate(sales_list):
                sales_amount = sale["price"] * sale["sales_quantity"]

                values = [
                    str(sale["sale_id"]),
                    str(sale["sale_date"]),
                    sale["product_name"],
                    f'{sale["price"]:,}',
                    str(sale["sales_quantity"]),
                    f"{sales_amount:,}",
                ]

                for column, value in enumerate(values):
                    item = QTableWidgetItem(value)

                    if column != 2:
                        item.setTextAlignment(Qt.AlignCenter)

                    self.sales_table.setItem(row, column, item)

        except RuntimeError as error:
            QMessageBox.critical(self, "데이터베이스 오류", str(error))

    def insert_sale(self):
        product_name = self.product_name_edit.text().strip()
        sale_date = self.sale_date_edit.date().toString("yyyy-MM-dd")
        price = self.price_spin_box.value()
        sales_quantity = self.sales_quantity_spin_box.value()

        if not product_name:
            QMessageBox.warning(self, "입력 오류", "상품명을 입력하세요.")
            self.product_name_edit.setFocus()
            return

        try:
            new_sale_id = self.db.insert_sale(
                sale_date,
                product_name,
                price,
                sales_quantity,
            )

            QMessageBox.information(
                self,
                "등록 완료",
                f"판매 정보가 등록되었습니다.\n번호: {new_sale_id}",
            )

            self.clear_inputs()
            self.load_sales()

        except RuntimeError as error:
            QMessageBox.critical(self, "등록 실패", str(error))

    def update_sale(self):
        sale_id_text = self.sale_id_edit.text().strip()

        if not sale_id_text:
            QMessageBox.warning(
                self,
                "선택 오류",
                "수정할 판매 정보를 표에서 선택하세요.",
            )
            return

        product_name = self.product_name_edit.text().strip()
        sale_date = self.sale_date_edit.date().toString("yyyy-MM-dd")
        price = self.price_spin_box.value()
        sales_quantity = self.sales_quantity_spin_box.value()

        if not product_name:
            QMessageBox.warning(self, "입력 오류", "상품명을 입력하세요.")
            return

        try:
            changed_rows = self.db.update_sale(
                int(sale_id_text),
                sale_date,
                product_name,
                price,
                sales_quantity,
            )

            if changed_rows == 0:
                QMessageBox.warning(
                    self,
                    "수정 실패",
                    "수정할 정보가 없거나 값이 변경되지 않았습니다.",
                )
                return

            QMessageBox.information(
                self,
                "수정 완료",
                "판매 정보가 수정되었습니다.",
            )

            self.clear_inputs()
            self.load_sales()

        except RuntimeError as error:
            QMessageBox.critical(self, "수정 실패", str(error))

    def delete_sale(self):
        sale_id_text = self.sale_id_edit.text().strip()

        if not sale_id_text:
            QMessageBox.warning(
                self,
                "선택 오류",
                "삭제할 판매 정보를 표에서 선택하세요.",
            )
            return

        answer = QMessageBox.question(
            self,
            "삭제 확인",
            "선택한 판매 정보를 삭제하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if answer != QMessageBox.Yes:
            return

        try:
            deleted_rows = self.db.delete_sale(int(sale_id_text))

            if deleted_rows == 0:
                QMessageBox.warning(
                    self,
                    "삭제 실패",
                    "삭제할 판매 정보를 찾을 수 없습니다.",
                )
                return

            QMessageBox.information(
                self,
                "삭제 완료",
                "판매 정보가 삭제되었습니다.",
            )

            self.clear_inputs()
            self.load_sales()

        except RuntimeError as error:
            QMessageBox.critical(self, "삭제 실패", str(error))

    def select_sale(self, row, column):
        items = [self.sales_table.item(row, index) for index in range(5)]

        if any(item is None for item in items):
            return

        sale_id = items[0].text()
        sale_date = QDate.fromString(items[1].text(), "yyyy-MM-dd")
        product_name = items[2].text()
        price = int(items[3].text().replace(",", ""))
        sales_quantity = int(items[4].text())

        self.sale_id_edit.setText(sale_id)
        self.sale_date_edit.setDate(sale_date)
        self.product_name_edit.setText(product_name)
        self.price_spin_box.setValue(price)
        self.sales_quantity_spin_box.setValue(sales_quantity)

    def clear_inputs(self):
        self.sale_id_edit.clear()
        self.sale_date_edit.setDate(QDate.currentDate())
        self.product_name_edit.clear()
        self.price_spin_box.setValue(0)
        self.sales_quantity_spin_box.setValue(0)

        self.sales_table.clearSelection()
        self.product_name_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
