import socket

#per ipv4 (af inet) e protocollo tcp(socket_stream)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host ='127.0.0.1'
port = 9898

#s.connect(host_server,port). da sottilineare che viene passata una tupla
s.connect(('127.0.0.1',9898))

s.send(b"client: connessione stabilita")

tm = s.recv(1024)
print(tm.decode())

s.close()
