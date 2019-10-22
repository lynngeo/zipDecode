from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QThread
import zipfile
from unrar import rarfile,unrarlib
import os,threading
import logging,sys
from python_Pratice.designDict import Ui_DialogDict

logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)


class Job(threading.Thread,QtCore.QObject):

    output = pyqtSignal(str)

    def __init__(self,filename,parent=None):
        threading.Thread.__init__(self)
        QtCore.QObject.__init__(self)
        self.flag = 1
        self.filename = filename


    def run(self):
        self.decryptRarZipFile(self.filename)

    def stop(self):
        self.flag = 0

    def decryptRarZipFile(self, filename):
        try:
            # 根据文件扩展名，使用不同的库
            if filename.endswith('.zip'):
                zFile = zipfile.ZipFile(filename)
            elif filename.endswith('.rar'):
                zFile = rarfile.RarFile(filename)
            # 解压缩的目标文件夹
            passwordfile = open('pwdlist.txt')

            for line in passwordfile.readlines():  # 逐行读取
                if self.flag == 1:
                    password = line.strip('\n')  # 去除换行符
                    try:
                        if filename.endswith('.zip'):
                            zFile.extractall(pwd=password.encode('ascii'))
                            self.output.emit('the password is: ' + password)
                            break  # 读取到正确密码就退出循环
                        elif filename.endswith('.rar'):

                            zFile.extractall(pwd=password)
                            self.output.emit('the password is: ' + password)
                            break  # 读取到正确密码就退出循环
                    except RuntimeError:
                        self.output.emit('wrong password: ' + password)
                        QApplication.processEvents()
                    except rarfile.BadRarFile:
                        self.output.emit('wrong password: ' + password)
                        QApplication.processEvents()
                    except TypeError as e:
                        self.output.emit(str(e))
                    except Exception as e:  # 打印报错
                        self.output.emit(str(e))
                elif self.flag == 0:
                    self.output.emit("停止破解")
                    break

        except Exception as e:  # 打印报错
            print(str(e))



class Ui_MainWindow(QtWidgets.QMainWindow):

    trigger = pyqtSignal(str)
    sin = pyqtSignal()
    dictsin = pyqtSignal()



    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.trigger.connect(self.update_text)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 550)
        MainWindow.setWindowTitle("压缩文件破解工具")
        #self.MainWindow = MainWindow
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 271, 31))
        self.textEdit.setObjectName("textEdit")


        self.label = QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(90, 29, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Aparajita")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(" 请选择或输入你要破解的文件路径")

        self.fileButton = QtWidgets.QPushButton(self.centralWidget)
        self.fileButton.setGeometry(QtCore.QRect(430, 70, 41, 31))
        self.fileButton.setObjectName("pushButton")
        self.fileButton.setText("...")

        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.startButton.setGeometry(QtCore.QRect(210, 130, 91, 41))
        self.startButton.setObjectName("startButton")
        self.cancelbutton = QtWidgets.QPushButton(self.centralWidget)
        self.cancelbutton.setGeometry(QtCore.QRect(310, 130, 91, 41))
        self.cancelbutton.setObjectName("cancelbutton")
        self.startButton.setText("开始破解")
        self.cancelbutton.setText("取消")


        self.showProcess = QtWidgets.QTextBrowser(self.centralWidget)
        self.showProcess.setGeometry(QtCore.QRect(168, 180, 302, 300))
        self.showProcess.setObjectName("processtext")

        MainWindow.setCentralWidget(self.centralWidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actiondict = QtWidgets.QAction(MainWindow)
        self.actiondict.setObjectName("actiondict")
        self.actionthread = QtWidgets.QAction(MainWindow)
        self.actionthread.setObjectName("actionthread")
        self.menu.addSeparator()
        self.menu.addAction(self.actiondict)
        self.menu.addAction(self.actionthread)
        self.menubar.addAction(self.menu.menuAction())

        self.menu.setTitle("工具")
        self.actiondict.setText("密码字典")
        self.actionthread.setText("线程数")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fileButton.clicked.connect(self.openfile)
        self.startButton.clicked.connect(lambda :self.startOrStopcrack(self.startButton.text()))
        self.cancelbutton.clicked.connect(lambda :self.startOrStopcrack(self.cancelbutton.text()))
        self.actiondict.triggered.connect(self.openDictWindow)

    def openDictWindow(self):
        try:

            dictDialog = QDialog()
            ui_Dict = Ui_DialogDict()
            ui_Dict.setupUi(dictDialog)
            dictDialog.show()
            dictDialog.exec_()
            #self.MainWindow.show()


        except Exception as e:
            print(e)



    def openfile(self):
        file_name = QFileDialog.getOpenFileName(self, '选择文件', '/', 'compressed files(*.zip , *.rar)')
        self.textEdit.setText(file_name[0])



    def startOrStopcrack(self,message=None):
        try:
            filename = self.textEdit.toPlainText()
            if filename == '':
                self.showProcess.setText("请输入或选择要破解的文件路径")
            else:
                job = Job(filename)
                self.sin.connect(job.stop)
                if message == "取消":
                    self.cancelbutton.setEnabled(False)
                    self.startButton.setEnabled(True)
                    self.sin.emit()
                if message == "开始破解":
                    self.cancelbutton.setEnabled(True)
                    self.startButton.setEnabled(False)
                    self.showProcess.clear()
                    job.flag = 1
                    if os.path.isfile(filename) and filename.endswith(('zip', 'rar')):
                        self.showProcess.setText("正在破解...")
                        job.start()
                        job.output.connect(self.update_text)
                    else:
                        self.trigger.emit('Must be Rar or Zip file')
        except Exception as e:
            print(e)

    def update_text(self,message):
        self.showProcess.append(message)



