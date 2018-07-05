import socket
sk = socket.socket()
sk.bind(("127.0.0.1",801))
#sk.bind(("10.243.99.78",801))
sk.listen(5)

conn,address = sk.accept()
sk.sendall(bytes("Hello world",encoding="utf-8"))
print(conn,address)