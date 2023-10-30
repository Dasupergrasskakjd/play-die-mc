# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from enums import gametoken
import random

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.texts = []
        self.tokens = []
        self.roles = {}
        self.label:QLabel = self.findChild(QLabel,"maintext")
        self.label.hide()
        self.startbutton:QPushButton = self.findChild(QPushButton,"startButton")
        self.startbutton.clicked.connect(self.start)
        self.nextbutton:QPushButton = self.findChild(QPushButton,"nextButton")
        self.nextbutton.clicked.connect(self.nextstep)
        self.lastbutton:QPushButton = self.findChild(QPushButton,"backButton")
        self.lastbutton.clicked.connect(self.laststep)
    def start(self):
        self.startbutton.hide()
        self.label.show()
    def nextstep(self):
        text = random.choice(['a','b','c'])
        self.texts.append(text)
        self.label.setText(text)
    def laststep(self):
        self.texts.pop(-1)
        if len(self.texts) == 0:return
        self.label.setText(self.texts[-1])
    def processtoken(self,token:gametoken):
        match token:
            case gametoken.GIVE_ROLES:
                self.sendroles()
    def sendroles(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
