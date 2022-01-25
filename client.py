import socket
import json
import time

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),5000))

msg = s.recv(1024)
omsg = msg.decode("utf-8")[1:-1]
title,value = omsg.split(":")
title = title.strip(' " " ')
title = title.capitalize()
print(title + ":" + value)