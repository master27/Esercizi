import socket

server = input ("inserire ip del server")
rangeInizio = input("inserire porta iniziale")
rangeFine = input ("inserire porta finale")

rangeInizio = int(rangeInizio)
rangeFine = int(rangeFine)

for port in range(rangeInizio, rangeFine):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    scansione = s.connect_ex((server, port))
    if scansione == 0:
        print("porta {} APERTA".format(port))
    else:
        print("porta {} CHIUSA".format(port))
    s.close()