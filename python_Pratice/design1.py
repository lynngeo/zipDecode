# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 300)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
#         self.buttonBox.setGeometry(QtCore.QRect(540, 80, 156, 23))
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEdit.setGeometry(QtCore.QRect(160, 70, 271, 31))
#         self.textEdit.setObjectName("textEdit")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(90, 29, 311, 31))
#         font = QtGui.QFont()
#         font.setFamily("Aparajita")
#         font.setPointSize(14)
#         font.setBold(False)
#         font.setWeight(50)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "zip破解工具"))
#         self.label.setText(_translate("MainWindow", "  请选择或输入你要破解的文件路径"))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#
#     sys.exit(app.exec())

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openfile = QAction(QIcon(r'C:\Users\Administrator\PycharmProjects\QT\picture\文件.jpg'),'open',self)
        openfile.setShortcut("Ctrl + 0")
        openfile.setStatusTip('open new file')
        openfile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        filemune = menubar.addMenu('$File')
        filemune.addAction(openfile)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('FIEL dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'open file', '/')
        if fname[0]:
            try:
                f = open(fname[0], 'r')
                with f:
                    data = f.read()
                    self.textEdit.setText(data)
            except:
                self.textEdit.setText("打开文件失败，可能是文件内型错误")

if __name__ == "__main__":
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

