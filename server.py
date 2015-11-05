#!usr/bin/env python
# -*- coding: utf-8 -*-  
#coding=utf-8  

from socket import *
from time import ctime

#IP
HOST=''
#端口号
PORT=3256
#长度
BUFSIZ=1024
#地址信息
ADDR=(HOST, PORT)

#建立服务端socket
tcpSerSock = socket( AF_INET, SOCK_STREAM)
#bind
tcpSerSock.bind(ADDR)
#监听
tcpSerSock.listen(5)

while True:
        #等待连接
        print 'waiting ....'
        tcpCliSock, addr = tcpSerSock.accept()
        print '.....connected from : ', addr

        while True:
            #读取数据
            while True:
                data = tcpCliSock.recv(BUFSIZ)
                if not data:
                    break

                #发送数据
                tcpCliSock.send(data)

        #关闭连接
        tcpCliSock.close()

#关闭服务端
tcpSerSock.close()


