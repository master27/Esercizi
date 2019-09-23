# https://docs.python.org/3/library/ftplib.html

from ftplib import FTP

server = "192.168.43.146"
ftp = FTP(server)
ftp.login(user="utente1", passwd="1234")

s= ftp.getwelcome()
f = ftp.dir()
f = str(f)
f = tuple(f)
print (type(f))

print (f)
