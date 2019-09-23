#definisco il comando da inviare in base al S.O.
#con platform.system() ho il tipo di sistema operativo utilizzato

import platform
import subprocess

ip = input("inserisci l'ip da pingare ")
ip = str(ip)
print (platform.machine())
# OLTRE L'ESERCIZIO: usi di uname e convertito a tupla.. fantastico!
print (platform.uname())
stato1 = platform.uname()
stato1 = tuple(stato1)
#print (type(stato1))
print ("...", stato1[0])
# FINE OLTRE L'ESERCIZIO
if platform.system() == "Linux":
    
    stato, risultato = subprocess.getstatusoutput("ping -c 5 "+ ip)
else:
    
    stato, risultato = subprocess.getstatusoutput("ping -n 5 "+ ip)
print (risultato)



