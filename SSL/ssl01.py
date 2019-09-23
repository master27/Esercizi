#Documentazione: https://docs.python.org/3/library/ssl.html
#script lato CLIENT
#GENERAZIONE CERTIFICATO LOCALE SELFSIGN:
#openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt

import ssl
import socket

host_addr = "127.0.0.1"
port = 8586

#FQDN definito durante la creazione delc ertificato
server_host_name = "esempio.com"
server_cert ="server.crt"

#server autentication utilizzando il certificato creato
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#conn = context.wrap_socket(s, server_side=False, server_hostname=server_host_name)
conn = context.wrap_socket(s, server_side=False, server_hostname=server_host_name)



conn.connect((host_addr,port))

print("connessione TSL/SSL")
