import socket
from urllib.parse import urlparse
#print (socket.getaddrinfo(127.0.0.1))
print (socket.gethostname())
print (socket.gethostbyaddr("192.168.8.37"))

url = "https://www.google.it"
# ottiene delle informazioni dall'url indicato
parsed = urlparse(url)
# attraverso il campo scheme si ottinene il tipo di porta
port = socket.getservbyname(parsed.scheme)

print (parsed, port)

# sito internet
print (parsed.netloc)
