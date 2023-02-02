from interface.ui_main_window import Ui_main_window
from PyQt5.QtWidgets import QWidget


class MainWidget(QWidget, Ui_main_window):
    def __init__(self):
        QWidget.__init__(self)
        Ui_main_window.__init__(self)
        self.setupUi(self)

    def setSubTitle(self, text):
        return

Main = MainWidget
