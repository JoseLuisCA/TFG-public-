from PySide6.QtGui import QDrag, QFont
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt


#Aquí definimos la página de la aplicación.
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoSandbox")
        self.setGeometry(100, 100, 800, 600)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home_page = self._build_home_page()
        self.fa_page = self._build_fa_page()

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.fa_page)
        self.stack.setCurrentWidget(self.home_page)

    #Página principal
    def _build_home_page(self) -> QWidget:
        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(40, 32, 40, 32)
        main_layout.setSpacing(24)

        title = QLabel("AutoSandbox", self)
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(28)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #1f2937;")

        buttons = QWidget()
        buttons_layout = QVBoxLayout(buttons)
        buttons_layout.setSpacing(16)

        button1 = QPushButton('Finite Automaton')
        button2 = QPushButton('Stack Automaton')
        button3 = QPushButton('Exit')

        for button in (button1, button2, button3):
            button.setMinimumHeight(64)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.setStyleSheet(
                "font-size: 18px;"
                "font-weight: 600;"
                "padding: 12px;"
            )

        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)
        buttons_layout.addWidget(button3)

        button1.clicked.connect(lambda: self.stack.setCurrentWidget(self.fa_page))
        button3.clicked.connect(self.close)

        main_layout.addWidget(title)
        main_layout.addWidget(buttons, 1)

        return container

    #Página de autómatas finitos
    def _build_fa_page(self) -> QWidget:
        page = QWidget()
        page_layout = QHBoxLayout(page)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.setSpacing(0)

        tool_menu = QWidget()
        tool_menu.setFixedWidth(90)
        tool_menu.setStyleSheet("background-color: #f3f4f6;")
        tool_layout = QVBoxLayout(tool_menu)
        tool_layout.setContentsMargins(12, 12, 12, 12)
        tool_layout.setSpacing(12)

        mouse_button = QPushButton("🖱")
        circle_button = QPushButton("○")
        arrow_button = QPushButton("➜")
        back_button = QPushButton("Back")

        for tool_button in (mouse_button, circle_button, arrow_button):
            tool_button.setMinimumHeight(56)
            tool_button.setStyleSheet(
                "font-size: 24px;"
                "background-color: white;"
                "border: 1px solid #d1d5db;"
                "border-radius: 10px;"
            )
            tool_layout.addWidget(tool_button)

        tool_layout.addStretch(1)

        back_button.setMinimumHeight(44)
        back_button.setStyleSheet(
            "font-size: 16px;"
            "font-weight: 600;"
            "background-color: white;"
            "border: 1px solid #d1d5db;"
            "border-radius: 10px;"
        )
        back_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.home_page))
        tool_layout.addWidget(back_button)

        workspace = QWidget()

        page_layout.addWidget(tool_menu)
        page_layout.addWidget(workspace, 1)

        return page


app = QApplication()
window = MainWindow()
window.show()

app.exec()