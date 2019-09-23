import socket

ip = "103.3.45.25"
portlist = [80,443,53,22,21,8080,8081,8082]

for i in portlist:
    mio =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scansione = mio.connect_ex((ip, i))
    print(i, ": ", scansione)
    mio.close()