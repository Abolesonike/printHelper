from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from interface.ui_main_window import Ui_main_window
from PyQt5.QtWidgets import QWidget
from functools import partial


class MainWidget(QWidget, Ui_main_window):
    def __init__(self):
        QWidget.__init__(self)
        Ui_main_window.__init__(self)
        self.setupUi(self)
        self.__initWidget()

    def setSubTitle(self, text):
        return

    @property
    def subStackList(self):
        return self.subStackWidget.subStackList

    @subStackList.setter
    def subStackList(self, value):
        self.subStackWidget.subStackList = value

    def __initWidget(self):
        self.navigationWidget.edit_btn.clicked.connect(
            partial(self.SwitchWidget, self.stackedWidget.indexOf(self.form)))
        self.navigationWidget.hsitory_btn.clicked.connect(
            partial(self.SwitchWidget, self.stackedWidget.indexOf(self.history)))
        self.stackedWidget1.setCurrentIndex(0)


    def SwitchWidget(self, index):
        sender = self.sender()
        if sender.text() == "填单":
            self.stackedWidget1.setCurrentIndex(0)
        elif sender.text() == "历史":
            self.stackedWidget1.setCurrentIndex(1)
        elif sender.text() == "数据维护":
            self.stackedWidget1.setCurrentIndex(2)

        return




Main = MainWidget
