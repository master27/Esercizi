#Visualizzazione dell'HEADER di un apgin html

import urllib.request
import urllib.error

try:
    url = "http://www.google.it"
    #prendo la risposta dell'url
    risposta = urllib.request.urlopen(url)
    print ("lo status code è: ", str(risposta.code))
    if risposta.code == 200:
        print (risposta.headers)                    #se il codei è 200 significa OK!
except urllib.error.URLError as errore:
    print ("URL non corretta ")
    print (errore.reason)
except urllib.error.HTTPError as errore2:
    print ("URL non corretta ")
    print (errore2.reason)

