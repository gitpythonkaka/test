
from socket import *

HOST='127.0.0.1'
PORT=32567
BUFSIZ=1024
ADDR=(HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break

    udpCliSock.sendto(data, ADDR)
    data = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break

    print 'recv : '
    print data

udpCliSock.close()

