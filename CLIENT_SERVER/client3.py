# Modifica: quanti byte invio (lezione client/server conteggio BYTE)
import socket

#per ipv4 (af inet) e protocollo tcp(socket_stream)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host ='127.0.0.1'
port = 9895

messaggio = bytearray("-"* 51 , "UTF-8")
s.connect((host,port))

s.send(b"messaggio CLIENT3")
#con recv_into abbiamo i byte del messagio
print(s.recv_into(messaggio))
print(messaggio)
