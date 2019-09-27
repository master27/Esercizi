#USER AGENT: http://www.useragentstring.com/
# sono le informazioni che possono essere ricavate da un client: tipo di browser, S.O. utilizzato ecc...
from urllib.request import Request
from urllib.request import urlopen

richiesta = Request ("http://www.google.it")
urlopen(richiesta)
print (richiesta.get_header("User-agent"))