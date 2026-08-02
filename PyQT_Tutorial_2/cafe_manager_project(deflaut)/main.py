import sys
from decimal import Decimal

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QDateEdit,
    QDialog,
    QDoubleSpinBox,
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
    QInputDialog,
    QApplication
)

from db_helper import DB, DB_CONFIG


def make_item(text, alignment=Qt.AlignCenter):
    item = QTableWidgetItem(str(text))
    item.setTextAlignment(alignment)
    return item


class IngredientWindow(QDialog):
    """원재료 재고 관리 전용 창."""

    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.db = db

        self.setWindowTitle("원재료 재고 관리")
        self.resize(900, 620)

        self.init_ui()
        self.connect_signals()
        self.load_ingredients()

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        title = QLabel("원재료 재고 관리")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            "font-size: 22px; font-weight: bold; padding: 8px;"
        )
        main_layout.addWidget(title)

        # 검색 영역
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("원재료 검색"))

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("원재료명을 입력하세요.")
        search_layout.addWidget(self.search_edit, 1)

        self.search_button = QPushButton("검색")
        self.show_all_button = QPushButton("전체 보기")
        search_layout.addWidget(self.search_button)
        search_layout.addWidget(self.show_all_button)

        main_layout.addLayout(search_layout)

        # 원재료 입력 영역
        input_group = QGroupBox("원재료 정보")
        input_layout = QHBoxLayout(input_group)

        self.ingredient_id_edit = QLineEdit()
        self.ingredient_id_edit.setReadOnly(True)
        self.ingredient_id_edit.setPlaceholderText("자동 생성")
        self.ingredient_id_edit.setFixedWidth(80)

        self.ingredient_name_edit = QLineEdit()
        self.ingredient_name_edit.setPlaceholderText("예: 원두")

        self.stock_spin = QDoubleSpinBox()
        self.stock_spin.setRange(0, 1_000_000)
        self.stock_spin.setDecimals(2)
        self.stock_spin.setFixedWidth(120)

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["개", "g", "kg", "ml", "L", "박스"])
        self.unit_combo.setEditable(True)
        self.unit_combo.setFixedWidth(90)

        self.minimum_stock_spin = QDoubleSpinBox()
        self.minimum_stock_spin.setRange(0, 1_000_000)
        self.minimum_stock_spin.setDecimals(2)
        self.minimum_stock_spin.setFixedWidth(120)

        input_layout.addWidget(QLabel("번호"))
        input_layout.addWidget(self.ingredient_id_edit)
        input_layout.addWidget(QLabel("원재료명"))
        input_layout.addWidget(self.ingredient_name_edit, 1)
        input_layout.addWidget(QLabel("현재 재고"))
        input_layout.addWidget(self.stock_spin)
        input_layout.addWidget(QLabel("단위"))
        input_layout.addWidget(self.unit_combo)
        input_layout.addWidget(QLabel("최소 재고"))
        input_layout.addWidget(self.minimum_stock_spin)

        main_layout.addWidget(input_group)

        # 버튼 영역
        button_layout = QHBoxLayout()

        self.insert_button = QPushButton("등록")
        self.update_button = QPushButton("수정")
        self.delete_button = QPushButton("삭제")
        self.order_button = QPushButton("주문")
        self.clear_button = QPushButton("초기화")
        self.refresh_button = QPushButton("새로고침")

        button_layout.addWidget(self.insert_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.order_button)
        button_layout.addStretch()
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.refresh_button)

        main_layout.addLayout(button_layout)

        # 원재료 목록
        self.ingredient_table = QTableWidget()
        self.ingredient_table.setColumnCount(6)
        self.ingredient_table.setHorizontalHeaderLabels(
            ["번호", "원재료명", "현재 재고", "단위", "최소 재고", "상태"]
        )
        self.ingredient_table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.ingredient_table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )
        self.ingredient_table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.ingredient_table.verticalHeader().setVisible(False)
        self.ingredient_table.verticalHeader().setDefaultSectionSize(34)
        self.ingredient_table.setAlternatingRowColors(True)

        header = self.ingredient_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.resizeSection(0, 65)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Fixed)
        header.resizeSection(2, 120)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        header.resizeSection(3, 85)
        header.setSectionResizeMode(4, QHeaderView.Fixed)
        header.resizeSection(4, 120)
        header.setSectionResizeMode(5, QHeaderView.Fixed)
        header.resizeSection(5, 100)

        self.ingredient_table.setStyleSheet(
            """
            QHeaderView::section {
                background: #e9ecef;
                font-weight: bold;
                border: 1px solid #d6d6d6;
                padding: 6px;
            }
            QTableWidget {
                gridline-color: #dddddd;
                alternate-background-color: #f8f9fa;
            }
            """
        )

        main_layout.addWidget(self.ingredient_table)

    def connect_signals(self):
        self.search_button.clicked.connect(self.search_ingredients)
        self.show_all_button.clicked.connect(self.show_all_ingredients)
        self.search_edit.returnPressed.connect(self.search_ingredients)

        self.insert_button.clicked.connect(self.insert_ingredient)
        self.update_button.clicked.connect(self.update_ingredient)
        self.delete_button.clicked.connect(self.delete_ingredient)
        self.order_button.clicked.connect(self.order_ingredient)
        self.clear_button.clicked.connect(self.clear_inputs)
        self.refresh_button.clicked.connect(self.load_ingredients)

        self.ingredient_table.cellClicked.connect(
            self.select_ingredient
        )

    def load_ingredients(self, keyword=""):
        try:
            rows = self.db.get_ingredients(keyword)
            self.ingredient_table.setRowCount(len(rows))

            for row_index, ingredient in enumerate(rows):
                stock = Decimal(str(ingredient["stock"]))
                minimum = Decimal(str(ingredient["minimum_stock"]))
                is_low = stock <= minimum
                status = "주문 필요" if is_low else "정상"

                values = [
                    ingredient["ingredient_id"],
                    ingredient["ingredient_name"],
                    f"{stock:,.2f}".rstrip("0").rstrip("."),
                    ingredient["unit"],
                    f"{minimum:,.2f}".rstrip("0").rstrip("."),
                    status,
                ]

                for column, value in enumerate(values):
                    alignment = (
                        Qt.AlignLeft | Qt.AlignVCenter
                        if column == 1
                        else Qt.AlignCenter
                    )
                    item = make_item(value, alignment)

                    if is_low:
                        item.setBackground(QColor("#fff3cd"))

                    self.ingredient_table.setItem(
                        row_index,
                        column,
                        item,
                    )

        except RuntimeError as error:
            QMessageBox.critical(self, "조회 실패", str(error))

    def search_ingredients(self):
        self.load_ingredients(self.search_edit.text().strip())

    def show_all_ingredients(self):
        self.search_edit.clear()
        self.load_ingredients()

    def insert_ingredient(self):
        name = self.ingredient_name_edit.text().strip()
        stock = self.stock_spin.value()
        unit = self.unit_combo.currentText().strip()
        minimum_stock = self.minimum_stock_spin.value()

        if not name:
            QMessageBox.warning(
                self,
                "입력 오류",
                "원재료명을 입력하세요.",
            )
            return

        if not unit:
            QMessageBox.warning(
                self,
                "입력 오류",
                "단위를 입력하세요.",
            )
            return

        try:
            new_id = self.db.insert_ingredient(
                name,
                stock,
                unit,
                minimum_stock,
            )
            QMessageBox.information(
                self,
                "등록 완료",
                f"원재료가 등록되었습니다.\n번호: {new_id}",
            )
            self.clear_inputs()
            self.load_ingredients()

        except RuntimeError as error:
            QMessageBox.critical(self, "등록 실패", str(error))

    def update_ingredient(self):
        ingredient_id = self.ingredient_id_edit.text().strip()

        if not ingredient_id:
            QMessageBox.warning(
                self,
                "선택 오류",
                "수정할 원재료를 표에서 선택하세요.",
            )
            return

        name = self.ingredient_name_edit.text().strip()
        unit = self.unit_combo.currentText().strip()

        if not name or not unit:
            QMessageBox.warning(
                self,
                "입력 오류",
                "원재료명과 단위를 입력하세요.",
            )
            return

        try:
            changed = self.db.update_ingredient(
                int(ingredient_id),
                name,
                self.stock_spin.value(),
                unit,
                self.minimum_stock_spin.value(),
            )

            if changed == 0:
                QMessageBox.warning(
                    self,
                    "수정 결과",
                    "변경된 내용이 없습니다.",
                )
                return

            QMessageBox.information(
                self,
                "수정 완료",
                "원재료 정보가 수정되었습니다.",
            )
            self.clear_inputs()
            self.load_ingredients()

        except RuntimeError as error:
            QMessageBox.critical(self, "수정 실패", str(error))

    def delete_ingredient(self):
        ingredient_id = self.ingredient_id_edit.text().strip()

        if not ingredient_id:
            QMessageBox.warning(
                self,
                "선택 오류",
                "삭제할 원재료를 표에서 선택하세요.",
            )
            return

        answer = QMessageBox.question(
            self,
            "삭제 확인",
            f"'{self.ingredient_name_edit.text()}' 원재료를 삭제하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if answer != QMessageBox.Yes:
            return

        try:
            deleted = self.db.delete_ingredient(int(ingredient_id))

            if deleted == 0:
                QMessageBox.warning(
                    self,
                    "삭제 실패",
                    "삭제할 원재료를 찾을 수 없습니다.",
                )
                return

            QMessageBox.information(
                self,
                "삭제 완료",
                "원재료가 삭제되었습니다.",
            )
            self.clear_inputs()
            self.load_ingredients()

        except RuntimeError as error:
            QMessageBox.critical(self, "삭제 실패", str(error))

    def order_ingredient(self):
        ingredient_id = self.ingredient_id_edit.text().strip()

        if not ingredient_id:
            QMessageBox.warning(
                self,
                "선택 오류",
                "주문할 원재료를 표에서 선택하세요.",
            )
            return

        quantity, ok = QInputDialog.getDouble(
            self,
            "원재료 주문",
            f"{self.ingredient_name_edit.text()} 주문 수량:",
            1.0,
            0.01,
            1_000_000,
            2,
        )

        if not ok:
            return

        try:
            self.db.order_ingredient(
                int(ingredient_id),
                quantity,
            )
            QMessageBox.information(
                self,
                "주문 완료",
                "주문 수량이 재고에 반영되었습니다.",
            )
            self.clear_inputs()
            self.load_ingredients()

        except RuntimeError as error:
            QMessageBox.critical(self, "주문 실패", str(error))

    def select_ingredient(self, row, column):
        items = [
            self.ingredient_table.item(row, index)
            for index in range(5)
        ]

        if any(item is None for item in items):
            return

        self.ingredient_id_edit.setText(items[0].text())
        self.ingredient_name_edit.setText(items[1].text())
        self.stock_spin.setValue(
            float(items[2].text().replace(",", ""))
        )
        self.unit_combo.setCurrentText(items[3].text())
        self.minimum_stock_spin.setValue(
            float(items[4].text().replace(",", ""))
        )

    def clear_inputs(self):
        self.ingredient_id_edit.clear()
        self.ingredient_name_edit.clear()
        self.stock_spin.setValue(0)
        self.unit_combo.setCurrentIndex(0)
        self.minimum_stock_spin.setValue(0)
        self.ingredient_table.clearSelection()
        self.ingredient_name_edit.setFocus()


class MainWindow(QMainWindow):
    """날짜별 상품 판매 관리 메인 창."""

    def __init__(self):
        super().__init__()

        self.db = DB(**DB_CONFIG)
        self.ingredient_window = None

        self.setWindowTitle("카페 판매 및 재고 관리")
        self.resize(1050, 700)

        self.init_ui()
        self.connect_signals()
        self.load_menu_combo()
        self.load_sales()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        title = QLabel("카페 판매 관리")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            "font-size: 24px; font-weight: bold; padding: 10px;"
        )
        main_layout.addWidget(title)

        # 검색 영역
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("상품 검색"))

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("상품명의 일부를 입력하세요. 예: 라떼")
        search_layout.addWidget(self.search_edit, 1)

        self.search_button = QPushButton("검색")
        self.show_all_button = QPushButton("전체 보기")
        self.ingredient_window_button = QPushButton("원재료 재고 관리")

        search_layout.addWidget(self.search_button)
        search_layout.addWidget(self.show_all_button)
        search_layout.addSpacing(20)
        search_layout.addWidget(self.ingredient_window_button)

        main_layout.addLayout(search_layout)

        # 판매 정보 수평 배치
        input_group = QGroupBox("판매 정보")
        input_layout = QHBoxLayout(input_group)

        self.sale_id_edit = QLineEdit()
        self.sale_id_edit.setReadOnly(True)
        self.sale_id_edit.setPlaceholderText("자동 생성")
        self.sale_id_edit.setFixedWidth(80)

        self.sale_date_edit = QDateEdit()
        self.sale_date_edit.setCalendarPopup(True)
        self.sale_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.sale_date_edit.setDate(QDate.currentDate())
        self.sale_date_edit.setFixedWidth(125)

        self.menu_combo = QComboBox()
        self.menu_combo.setMinimumWidth(220)

        self.price_edit = QLineEdit()
        self.price_edit.setReadOnly(True)
        self.price_edit.setFixedWidth(120)

        self.sales_quantity_spin = QSpinBox()
        self.sales_quantity_spin.setRange(0, 100_000)
        self.sales_quantity_spin.setSuffix(" 잔")
        self.sales_quantity_spin.setFixedWidth(110)

        input_layout.addWidget(QLabel("번호"))
        input_layout.addWidget(self.sale_id_edit)
        input_layout.addWidget(QLabel("날짜"))
        input_layout.addWidget(self.sale_date_edit)
        input_layout.addWidget(QLabel("상품명"))
        input_layout.addWidget(self.menu_combo, 1)
        input_layout.addWidget(QLabel("가격"))
        input_layout.addWidget(self.price_edit)
        input_layout.addWidget(QLabel("판매량"))
        input_layout.addWidget(self.sales_quantity_spin)

        main_layout.addWidget(input_group)

        # 버튼 영역
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

        main_layout.addLayout(button_layout)

        # 판매 목록
        self.sales_table = QTableWidget()
        self.sales_table.setColumnCount(6)
        self.sales_table.setHorizontalHeaderLabels(
            ["번호", "날짜", "상품명", "가격", "판매량", "매출액"]
        )
        self.sales_table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.sales_table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )
        self.sales_table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.sales_table.verticalHeader().setVisible(False)
        self.sales_table.verticalHeader().setDefaultSectionSize(36)
        self.sales_table.setAlternatingRowColors(True)

        header = self.sales_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.resizeSection(0, 65)
        header.setSectionResizeMode(1, QHeaderView.Fixed)
        header.resizeSection(1, 120)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        header.resizeSection(3, 110)
        header.setSectionResizeMode(4, QHeaderView.Fixed)
        header.resizeSection(4, 90)
        header.setSectionResizeMode(5, QHeaderView.Fixed)
        header.resizeSection(5, 125)

        self.sales_table.setStyleSheet(
            """
            QHeaderView::section {
                background: #e9ecef;
                font-weight: bold;
                border: 1px solid #d6d6d6;
                padding: 6px;
            }
            QTableWidget {
                gridline-color: #dddddd;
                alternate-background-color: #f8f9fa;
            }
            """
        )

        main_layout.addWidget(self.sales_table)

        ## 최 하단 설정
        summary_layout = QHBoxLayout()


        self.summary_label = QLabel("총 판매량: 0잔 | 총 매출액: 0원")
        self.summary_label.setAlignment(Qt.AlignRight)
        self.summary_label.setStyleSheet(
            "font-size: 18px; font-weight: bold; padding: 8px;"
        )

        self.back_btn = QPushButton("뒤로가기")
        summary_layout.addWidget(self.summary_label)
        summary_layout.addStretch()
        summary_layout.addWidget(self.back_btn)

        main_layout.addLayout(summary_layout)

    def connect_signals(self):
        self.search_button.clicked.connect(self.search_sales)
        self.show_all_button.clicked.connect(self.show_all_sales)
        self.search_edit.returnPressed.connect(self.search_sales)
        self.search_edit.textChanged.connect(self.search_sales)

        self.ingredient_window_button.clicked.connect(
            self.open_ingredient_window
        )

        self.menu_combo.currentIndexChanged.connect(
            self.update_price_display
        )

        self.insert_button.clicked.connect(self.insert_sale)
        self.update_button.clicked.connect(self.update_sale)
        self.delete_button.clicked.connect(self.delete_sale)
        self.clear_button.clicked.connect(self.clear_inputs)
        self.refresh_button.clicked.connect(self.load_sales)

        self.sales_table.cellClicked.connect(self.select_sale)

    def load_menu_combo(self):
        try:
            menus = self.db.get_all_menus()

            self.menu_combo.blockSignals(True)
            self.menu_combo.clear()

            for menu in menus:
                self.menu_combo.addItem(
                    menu["product_name"],
                    {
                        "menu_id": menu["menu_id"],
                        "price": menu["price"],
                    },
                )

            self.menu_combo.blockSignals(False)
            self.update_price_display()

        except RuntimeError as error:
            QMessageBox.critical(
                self,
                "메뉴 조회 실패",
                str(error),
            )

    def update_price_display(self):
        data = self.menu_combo.currentData()

        if not data:
            self.price_edit.clear()
            return

        self.price_edit.setText(f'{data["price"]:,} 원')

    def load_sales(self, keyword=""):
        try:
            sales = self.db.get_sales(keyword)
            self.sales_table.setRowCount(len(sales))

            total_quantity = 0
            total_amount = 0

            for row_index, sale in enumerate(sales):
                sales_amount = (
                    sale["price"] * sale["sales_quantity"]
                )
                total_quantity += sale["sales_quantity"]
                total_amount += sales_amount

                values = [
                    sale["sale_id"],
                    sale["sale_date"],
                    sale["product_name"],
                    f'{sale["price"]:,}',
                    sale["sales_quantity"],
                    f"{sales_amount:,}",
                ]

                for column, value in enumerate(values):
                    alignment = (
                        Qt.AlignLeft | Qt.AlignVCenter
                        if column == 2
                        else Qt.AlignCenter
                    )
                    self.sales_table.setItem(
                        row_index,
                        column,
                        make_item(value, alignment),
                    )

            self.summary_label.setText(
                f"총 판매량: {total_quantity:,}잔 | "
                f"총 매출액: {total_amount:,}원"
            )

        except RuntimeError as error:
            QMessageBox.critical(
                self,
                "판매 내역 조회 실패",
                str(error),
            )

    def search_sales(self):
        self.load_sales(self.search_edit.text().strip())

    def show_all_sales(self):
        self.search_edit.clear()
        self.load_sales()

    def insert_sale(self):
        menu_data = self.menu_combo.currentData()

        if not menu_data:
            QMessageBox.warning(
                self,
                "입력 오류",
                "등록할 메뉴를 선택하세요.",
            )
            return

        try:
            new_id = self.db.insert_sale(
                self.sale_date_edit.date().toString(
                    "yyyy-MM-dd"
                ),
                menu_data["menu_id"],
                self.sales_quantity_spin.value(),
            )

            QMessageBox.information(
                self,
                "등록 완료",
                f"판매 정보가 등록되었습니다.\n번호: {new_id}",
            )
            self.clear_inputs()
            self.load_sales(self.search_edit.text().strip())

        except RuntimeError as error:
            QMessageBox.critical(self, "등록 실패", str(error))

    def update_sale(self):
        sale_id = self.sale_id_edit.text().strip()
        menu_data = self.menu_combo.currentData()

        if not sale_id:
            QMessageBox.warning(
                self,
                "선택 오류",
                "수정할 판매 내역을 선택하세요.",
            )
            return

        if not menu_data:
            return

        try:
            changed = self.db.update_sale(
                int(sale_id),
                self.sale_date_edit.date().toString(
                    "yyyy-MM-dd"
                ),
                menu_data["menu_id"],
                self.sales_quantity_spin.value(),
            )

            if changed == 0:
                QMessageBox.warning(
                    self,
                    "수정 결과",
                    "변경된 내용이 없습니다.",
                )
                return

            QMessageBox.information(
                self,
                "수정 완료",
                "판매 정보가 수정되었습니다.",
            )
            self.clear_inputs()
            self.load_sales(self.search_edit.text().strip())

        except RuntimeError as error:
            QMessageBox.critical(self, "수정 실패", str(error))

    def delete_sale(self):
        sale_id = self.sale_id_edit.text().strip()

        if not sale_id:
            QMessageBox.warning(
                self,
                "선택 오류",
                "삭제할 판매 내역을 선택하세요.",
            )
            return

        answer = QMessageBox.question(
            self,
            "삭제 확인",
            "선택한 판매 내역을 삭제하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if answer != QMessageBox.Yes:
            return

        try:
            deleted = self.db.delete_sale(int(sale_id))

            if deleted == 0:
                QMessageBox.warning(
                    self,
                    "삭제 실패",
                    "삭제할 판매 내역을 찾을 수 없습니다.",
                )
                return

            QMessageBox.information(
                self,
                "삭제 완료",
                "판매 내역이 삭제되었습니다.",
            )
            self.clear_inputs()
            self.load_sales(self.search_edit.text().strip())

        except RuntimeError as error:
            QMessageBox.critical(self, "삭제 실패", str(error))

    def select_sale(self, row, column):
        sale_id_item = self.sales_table.item(row, 0)
        date_item = self.sales_table.item(row, 1)
        product_item = self.sales_table.item(row, 2)
        quantity_item = self.sales_table.item(row, 4)

        if any(
            item is None
            for item in (
                sale_id_item,
                date_item,
                product_item,
                quantity_item,
            )
        ):
            return

        self.sale_id_edit.setText(sale_id_item.text())
        self.sale_date_edit.setDate(
            QDate.fromString(date_item.text(), "yyyy-MM-dd")
        )

        index = self.menu_combo.findText(product_item.text())
        if index >= 0:
            self.menu_combo.setCurrentIndex(index)

        self.sales_quantity_spin.setValue(
            int(quantity_item.text().replace(",", ""))
        )

    def clear_inputs(self):
        self.sale_id_edit.clear()
        self.sale_date_edit.setDate(QDate.currentDate())
        self.sales_quantity_spin.setValue(0)

        if self.menu_combo.count() > 0:
            self.menu_combo.setCurrentIndex(0)

        self.sales_table.clearSelection()

    def open_ingredient_window(self):
        if (
            self.ingredient_window is None
            or not self.ingredient_window.isVisible()
        ):
            self.ingredient_window = IngredientWindow(
                self.db,
                self,
            )

        self.ingredient_window.show()
        self.ingredient_window.raise_()
        self.ingredient_window.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)


    w = MainWindow()
    w.show()
    sys.exit(app.exec_()) # 창 닫으면 프로그램 종료
