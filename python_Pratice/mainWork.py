from PyQt5.QtWidgets import QApplication ,QMainWindow
from python_Pratice.design import Ui_MainWindow





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())