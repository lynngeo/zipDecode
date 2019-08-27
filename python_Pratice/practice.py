#encoding:utf-8
from Tkinter import *


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel =Label(self,text='hello,world')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()





app = Application()
app.master.title('压缩文件解密')
app.mainloop()