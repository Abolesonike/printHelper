from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QScroller, QTableWidget
from PyQt5.QtGui import QMouseEvent

class BaseTableWidget(QTableWidget):
    def __init__(self, parent):
        QTableWidget.__init__(self, parent)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)




