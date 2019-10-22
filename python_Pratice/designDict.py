# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designDict.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_DialogDict(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_DialogDict, self).__init__()
        self.setupUi(self)


    def accept(self):
        pass

    def reject(self):
        pass

    def MainWindow(self):
        pass


    def setupUi(self, DialogDict):
        DialogDict.setObjectName("DialogDict")
        DialogDict.resize(400, 416)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogDict)
        self.buttonBox.setGeometry(QtCore.QRect(20, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DialogDict)
        self.label.setGeometry(QtCore.QRect(50, 50, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogDict)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 231, 16))
        self.label_2.setObjectName("label_2")
        self.shortLength = QtWidgets.QLineEdit(DialogDict)
        self.shortLength.setEnabled(True)
        self.shortLength.setGeometry(QtCore.QRect(80, 210, 61, 20))
        self.shortLength.setMouseTracking(True)
        self.shortLength.setInputMask("")
        self.shortLength.setObjectName("shortLength")
        self.label_3 = QtWidgets.QLabel(DialogDict)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DialogDict)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 151, 16))
        self.label_4.setObjectName("label_4")
        self.filename_line = QtWidgets.QLineEdit(DialogDict)
        self.filename_line.setGeometry(QtCore.QRect(60, 300, 221, 20))
        self.filename_line.setObjectName("filename_line")
        self.longlength = QtWidgets.QLineEdit(DialogDict)
        self.longlength.setGeometry(QtCore.QRect(220, 210, 61, 20))
        self.longlength.setObjectName("longlength")
        self.fileButton = QtWidgets.QPushButton(DialogDict)
        self.fileButton.setGeometry(QtCore.QRect(280, 300, 37, 21))
        self.fileButton.setObjectName("fileButton")
        self.specialCharacterEdit = QtWidgets.QLineEdit(DialogDict)
        self.specialCharacterEdit.setGeometry(QtCore.QRect(150, 130, 171, 27))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        self.specialCharacterEdit.setFont(font)
        self.specialCharacterEdit.setObjectName("specialCharacterEdit")
        self.checkBox = QtWidgets.QCheckBox(DialogDict)
        self.checkBox.setGeometry(QtCore.QRect(60, 90, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(DialogDict)
        self.checkBox_2.setGeometry(QtCore.QRect(210, 90, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.widget = QtWidgets.QWidget(DialogDict)
        self.widget.setGeometry(QtCore.QRect(60, 130, 212, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)

        self.retranslateUi(DialogDict)
        self.buttonBox.accepted.connect(DialogDict.accept)
        self.buttonBox.rejected.connect(DialogDict.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDict)

        self.fileButton.clicked.connect(self.openfile)

    def retranslateUi(self, DialogDict):
        _translate = QtCore.QCoreApplication.translate
        DialogDict.setWindowTitle(_translate("DialogDict", "字典选择"))
        self.label.setText(_translate("DialogDict", "请选择生成字典的组成元素"))
        self.label_2.setText(_translate("DialogDict", "请选择生成密码的长度（默认长度1~10位）"))
        self.shortLength.setText(_translate("DialogDict", "1"))
        self.label_3.setText(_translate("DialogDict", "至"))
        self.label_4.setText(_translate("DialogDict", "可以选择你自己的字典哦"))
        self.longlength.setText(_translate("DialogDict", "10"))
        self.fileButton.setText(_translate("DialogDict", "..."))
        self.specialCharacterEdit.setText(_translate("DialogDict", "可以补充你自己的特殊字符"))
        self.checkBox.setText(_translate("DialogDict", "数字"))
        self.checkBox_2.setText(_translate("DialogDict", "字母"))
        self.checkBox_3.setText(_translate("DialogDict", "特殊字符"))


    def openfile(self):
        try:
            file_name = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '/', 'text files(*.txt)')
            self.filename_line.setText(file_name[0])
        except Exception as e:
            print(e)