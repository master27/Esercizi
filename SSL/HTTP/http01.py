import http.client

connessione = http.client.HTTPConnection("www.httpbin.org")

connessione.request("GET", "/forms/post")

rispostaServer = connessione.getresponse()

#print(rispostaServer)
print(rispostaServer.status, rispostaServer.reason)

dati = rispostaServer.read()

print (dati.decode())

#ctrs W