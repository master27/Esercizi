#esecuzione di un comando (ping)

import subprocess
import socket
ip = "127.0.0.1"

stato, risultato = subprocess.getstatusoutput("ping -c 2 " + ip)
print (risultato)