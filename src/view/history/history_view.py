from PyQt5.QtWidgets import QWidget
from interface.ui_history import Ui_History


class HistoryView(QWidget, Ui_History):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        Ui_History.__init__(self)
        self.setupUi(self)
