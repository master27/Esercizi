'''

CREAZIONE CLIENT SOCKET:
------------------------
1- Creazione SOCKET                     socket.socket
2- Connessione al Server                connet(indirizzo)
3- Invio di una richiesta al server     send()
4- Ricezione di una risposta dal server recv()

'''
import socket
import sys

def invia_comandi(s):
    while True:
        comando = input("--> ")
        if comando == "ESC":
            print("chiudo la connessione")
            s.close()
        else:
            s.send(comando.encode())
            data = s.recv(4096)
            print(str(data, "utf-8"))

def conn_sub_server(indirizzo_server):
    try:
        s = socket.socket()             #creazione del SOCKET Client
        s.connect(indirizzo_server)     #connessione al server
        print(f"connessione al server {indirizzo_server} stabilita")
    except socket.error as errore:
        print(f"qualcosa è andato storto...\n{errore}")
        sys.exit()
    invia_comandi(s)


if __name__ =="__main__":
    conn_sub_server(("192.168.8.37", 15000))
