#!usr/bin/env python
# -*- coding: utf-8 -*-  
#coding=utf-8  

from socket import *
from time import ctime

#IP
HOST=''
#端口号
PORT=32567
#长度
BUFSIZ=1024
#地址信息
ADDR=(HOST, PORT)

#建立服务端socket
udpSerSock = socket( AF_INET, SOCK_DGRAM)
#bind
udpSerSock.bind(ADDR)

while True:
        #等待连接
        print 'waiting ....'
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        print '.....connected from : ', addr
        #发送数据
        udpSerSock.sendto(data, addr)

#关闭服务端
udpSerSock.close()


