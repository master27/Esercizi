# controllo dell'exit code (risultato)

import subprocess

ip = "127.0.0.1"

stato,risultato = subprocess.getstatusoutput("ping -c 2 "+ ip)

if stato == 0:
    print("il sistema: "+ ip + " è attivo ")
else:
    print("il sistema: "+ ip + " è down ")