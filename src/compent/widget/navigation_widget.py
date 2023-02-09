from interface.ui_navigation import Ui_Navigation
from PyQt5.QtWidgets import QWidget, QMessageBox


class NavigationWidget(QWidget, Ui_Navigation):
    def __init__(self, parent = None):
        QWidget.__init__(self)
        Ui_Navigation.__init__(self)
        self.setupUi(self)
        self.resize(260, 800)
