import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


menu_form = uic.loadUiType("menu.ui")[0]


class MenuPage(QWidget, menu_form):
    def __init__(self, show_inventory):
        super().__init__()
        self.setupUi(self)

        # menu.ui에 inventoryButton이라는 버튼이 있다고 가정
        self.pushButton.clicked.connect(show_inventory)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedWidget 예제")
        self.resize(400, 300)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.page1 = MenuPage(self.show_inventory)
        self.page2 = self.create_inventory_page()

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

    def create_inventory_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        self.label = QLabel("재고 화면")
        self.label.setAlignment(Qt.AlignCenter)

        back_button = QPushButton("뒤로가기")
        back_button.clicked.connect(self.show_menu)

        layout.addWidget(self.label)
        layout.addWidget(back_button)

        return page

    def show_inventory(self):
        self.label.setText("재고 목록입니다.")
        self.stack.setCurrentWidget(self.page2)

    def show_menu(self):
        self.stack.setCurrentWidget(self.page1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())