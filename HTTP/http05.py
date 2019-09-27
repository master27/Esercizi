#USER AGENT: manipolazione dell'HEADEWR

from urllib.request import Request
from urllib.request import urlopen

richiesta = Request("http://www.debian.org")

richiesta.add_header("Accept-Language", "fr")
risposta = urlopen(richiesta)
risposta2 = risposta.read()

print (risposta2.decode())