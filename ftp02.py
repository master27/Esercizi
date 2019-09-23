# https://docs.python.org/3/library/ftplib.html
# Trasferimento file FTP

from ftplib import FTP

server = "192.168.43.146"
ftp = FTP(server)
ftp.login(user="utente1", passwd="1234")

s= ftp.getwelcome()
#ftp.mkd("Numero1")
f = ftp.dir()

filename = "testo.txt"
file = open(filename, "wb")
ftp.retrbinary("RETR" + filename, file.write)

file.close()


print (f)
