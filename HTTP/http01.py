import http.client
import os

connessione = http.client.HTTPConnection("www.httpbin.org")

connessione.request("GET", "/forms/post")

rispostaServer = connessione.getresponse()

#print(rispostaServer)
print(rispostaServer.status, rispostaServer.reason)

dati = rispostaServer.read()
#creo un file e ci scrivo il codice ricavato
f = open("sito.txt", "w")
f.write(dati.decode())


print (dati.decode())

#ctrs W