#modifica: utilizzo del protocollo UDP
#modifica (timeout)
import socket

host = "127.0.0.1"
port = 12345
# SOCK_DGRAM definisce il protocollo udp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind((host, port))
    s.settimeout(5)

#recvfrom perchè si usa UDP
    data, addr = s.recvfrom(1024)
    print (addr)

    print("La stringa ricevuta è: ", data.decode())

    s.close()
except socket.timeout as e:
    print("tempo scaduto!!!", {e.strerror})
    s.close()