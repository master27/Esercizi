#modifica: utilizzo del protocollo UDP
import socket

host = "127.0.0.1"
port = 12345
# SOCK_DGRAM definisce il protocollo udp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))

data, addr = s.recvfrom(1024)
print (addr)

print("La stringa ricevuta è: ", data.decode())

s.close()