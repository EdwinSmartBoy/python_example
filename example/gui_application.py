# -*- coding: utf-8 -*-
"""
-----------------------------------------
  IDEA Name    :  PyCharm  
  Project Name :  python_example
-----------------------------------------
  File Name    :  gui_application
  Description  :
  Author       :  Edwin
  Date         :  2018/1/6 22:14
-----------------------------------------
  Changer      :  Edwin
  Date         :  2018/1/6 22:14
  Description  :  
-----------------------------------------
"""
__author__ = 'Edwin'

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, World!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit())
        self.quitButton.pack()


if __name__ == '__main__':
    app = Application()
    app.master.title('Hello, World!')
    app.mainloop()
