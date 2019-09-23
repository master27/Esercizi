#modifica: calcolare i byte ricevuti/inviati

import socket

#creare oggetto di tipo socket _stream per protocollo TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip Server e porta
host = "127.0.0.1"
port = 9895

#bind della connessione. i 3 parametri sono il protocollo con SOCK_STREAAM(tcp) HOST E PORTA
serversocket.bind((host, port))

#server in ascolto per 4 connessioni
serversocket.listen(4)

while True:
    #accettare le connessioni, come parametro in uscita dobbiamo avere 2 variabili: il client socket e l'indirizzo client
    clientsocket, addr = serversocket.accept()
    #visualizzo la porta client che è dinamica
    #print (addr)
    #grandezza buffer del pacchetto
    mr = clientsocket.recv(1024)
    print (mr.decode())
    #invio del messaggio in modalità byte
    clientsocket.send(b"Messaggio da parte del server")
    clientsocket.close()



