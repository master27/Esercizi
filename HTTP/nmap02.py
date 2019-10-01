import nmap

primo_port_scan = nmap.PortScanner()
prima_scansione = primo_port_scan.scan("127.0.0.1", "22, 80, 53", "-sS")

for host in primo_port_scan.all_hosts():
    print ("L'host in questione è: ", host)
    print ("il suo stato è: ", primo_port_scan[host].state())

    for protocollo in primo_port_scan[host].all_protocols():
        print("Il protocollo è :", protocollo)
        port = primo_port_scan[host][protocollo].keys()
        for porte in port:
            print ("Porta Numero: ", porte, " stato ", primo_port_scan[host][protocollo][porte]["state"])

