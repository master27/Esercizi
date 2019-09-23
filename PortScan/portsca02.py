import socket


def portscan(ip, listaporte):
    for port in listaporte:
        mio = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        scansione = mio.connect_ex((ip, port))

        if scansione == 0:
            print("porta {} APERTA".format(port))
        else:
            print("porta {} CHIUSA".format(port))
        mio.close()

portscan("127.0.0.1",[22,80,4444])

