import json
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5000))
s.listen(5)
currenttime = time.time()
time = {"time":int(currenttime)}
time_json = json.dumps(time)
while True:
    clientsocket, address = s.accept()
    clientsocket.send(bytes(time_json,"utf-8"))