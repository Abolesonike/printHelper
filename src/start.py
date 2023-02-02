if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    from src.compent.widget.mian_widget import MainWidget
    from view.form.form_view import FormView
    from src.interface.ui_form import Ui_Form

    main = MainWidget()
    main.show()  # 显示窗体
    sys.exit(app.exec_())