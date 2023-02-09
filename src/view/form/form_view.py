from PyQt5.QtWidgets import QWidget, QMessageBox
from interface.ui_form import Ui_Form

class FormView(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        Ui_Form.__init__(self)
        self.setupUi(self)
        self.__initForm()

    def __initForm(self):
        self.printBtn.clicked.connect(self.print)

    def print(self):
        QMessageBox.information(self, "打印成功", "", QMessageBox.Yes)
