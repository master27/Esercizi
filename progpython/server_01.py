'''
CREAZIONE LATO SERVER

1- Creazione Socket                                                         socket.socket()
2- Collegamento del socket all'indirizzo del srv e alla porta designata     bind()
3- messa in ascolto in attesa della connessione Client                      listen()
4 -Accettazione del Client                                                  accept()
5- Ricezione richiesta Cleint                                               recv()
6- Elaborazione di una risposta                                             subprocess()
7- Invio risposta al client                                                 send()  

'''
import socket
import subprocess
import sys

def ricevi_comandi(conn):
    while True:
        richiesta = conn.recv(4096)
        risposta = subprocess.run(richiesta.decode(), shell=True, stdout =subprocess.PIPE, stderr = subprocess.PIPE)
        data = risposta.stdout + risposta.stderr
        conn.send(data)


#backlog sono il numero delle connessioni non accettate ma ammesse 
def sub_server(indirizzo, backlog=1):
    try:
        s = socket.socket()             #creazione del socket
        s.bind(indirizzo)
        s.listen(backlog)               #mettiti in ascolto per un massimo di richieste di backlog
        print("server inizializzato, ora in ascolto..")
    except socket.error as errore:
        print(f"qualcosa non è andato bene.. \n{errore}")
        print("reinizializzo ils server")
        sub_server(indirizzo, backlog=1)
    conn, indirizzo_client = s.accept()         # dove ricevo come risposta conenssione eindirizo client
    print("connessione al server eseguita...{indirizzo_client}")
    ricevi_comandi(conn)

if __name__ == "__main__":
    sub_server(("", 15000))