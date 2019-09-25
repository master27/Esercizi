#gestione errori
import urllib.request

try:
    risposta = urllib.request.urlopen("htp://www.google.it")
    print(risposta.read())
    risposta.close()
except urllib.request.URLError as errore:
    print (errore.reason)
