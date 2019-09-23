# MODIFICA client per trasmissione UDP

import socket

host = ("127.0.0.1")
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print (s.sendto(b"ciao!", (host, port)))