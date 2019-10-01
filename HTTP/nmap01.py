import nmap

scansione = nmap.PortScanner()

risultato = scansione.scan("192.168.60.2", "22", "-sS")

#print (dict(risultato))
#print (risultato.)
print (scansione.scaninfo())
