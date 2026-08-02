from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QPushButton,
    QToolButton,
    QApplication
)
import sys

form_class = uic.loadUiType("menuedit.ui")[0]


class MenuManageDialog(QDialog, form_class):
    COLUMN_COUNT = 4

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.db = db
        self.current_category = "커피"

        self.bestButton.clicked.connect(
            lambda: self.change_category("베스트")
        )
        self.coffeeButton.clicked.connect(
            lambda: self.change_category("커피")
        )
        self.adeButton.clicked.connect(
            lambda: self.change_category("에이드")
        )
        self.etcButton.clicked.connect(
            lambda: self.change_category("기타")
        )

        self.closeButton.clicked.connect(self.close)

        self.load_menu_cards()

    def change_category(self, category):
        self.current_category = category
        self.load_menu_cards()

    def clear_menu_grid(self):
        while self.menuGridLayout.count():
            item = self.menuGridLayout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    def load_menu_cards(self):
        self.clear_menu_grid()

        menu_list = self.db.get_menus_by_category(
            self.current_category
        )

        for index, menu in enumerate(menu_list):
            row = index // self.COLUMN_COUNT
            column = index % self.COLUMN_COUNT

            card = self.create_menu_card(menu)

            self.menuGridLayout.addWidget(
                card,
                row,
                column,
            )

        add_index = len(menu_list)
        add_row = add_index // self.COLUMN_COUNT
        add_column = add_index % self.COLUMN_COUNT

        add_button = self.create_add_button()

        self.menuGridLayout.addWidget(
            add_button,
            add_row,
            add_column,
        )

    def create_menu_card(self, menu):
        button = QToolButton()

        button.setText(
            f'{menu["product_name"]}\n'
            f'{menu["price"]:,}원'
        )

        button.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon
        )

        button.setMinimumSize(150, 190)

        button.clicked.connect(
            lambda checked=False, menu_id=menu["menu_id"]:
            self.open_edit_dialog(menu_id)
        )

        return button

    def create_add_button(self):
        button = QPushButton("+\n메뉴 추가")
        button.setMinimumSize(150, 190)

        button.clicked.connect(
            self.open_add_dialog
        )

        return button

    def open_add_dialog(self):
        dialog = AddMenuDialog(
            self.db,
            self.current_category,
            self,
        )

        if dialog.exec_() == QDialog.Accepted:
            self.load_menu_cards()

    def open_edit_dialog(self, menu_id):
        dialog = EditMenuDialog(
            self.db,
            menu_id,
            self,
        )

        if dialog.exec_() == QDialog.Accepted:
            self.load_menu_cards()

app = QApplication(sys.argv)

w = MenuManageDialog()
w.show()

app.exec_()