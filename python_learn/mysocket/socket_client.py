import socket

obj = socket.socket()
obj.connect(("10.243.99.78",8080))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)