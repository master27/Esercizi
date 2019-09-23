#Documentazione: https://docs.python.org/3/library/ssl.html
#script lato SERVER

import ssl
import socket

host_addr = "127.0.0.1"
port = 8586

server_cert = "server.crt"
server_key = "server.key"

#uso TLS protocol

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#carico certificato e chiave
context.load_cert_chain(certfile=server_cert, keyfile=server_key)

bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindsocket.bind((host_addr, port))
bindsocket.listen(5)
print("in attesa di connessione")

newsocket, addr =bindsocket.accept()
print("connessione stabilita", addr)

#applico al socket creato il TLS
conn = context.wrap_socket(newsocket, server_side=True)
data = conn.recv(1024)
conn.close()