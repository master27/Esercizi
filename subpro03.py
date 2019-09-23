#PING scan dato in ingresso ip di partenza e ip finale
import subprocess

net = input("inserisci l'indirizzo di rete /24 ")
start = input("valore di partenza: ")
end = input("valore finale: ")

#l'elemento discirminante della tringa in ingresso è il . es: 192.168.0.100 Split divide i valori

net1 = net.split(".")

a = "."
# cast di trasformazione da str a int
start = int(start)
end = int(end)
contatore = end - start

for coutn in range(contatore):
    start = str(start)
    addressStart = net1[0] + a + net1[1] + a +net1[2] + a + start
    stato,risultato = subprocess.getstatusoutput("ping  -c 3 " + addressStart)
    start = int(start)
    start += 1
    start = str(start)
    print(risultato)

'''
print (net1[0])
print (net1[1])
print (net1[2])
print (net1[3])
'''