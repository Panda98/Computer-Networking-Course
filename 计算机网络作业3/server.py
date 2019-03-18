#!/usr/bin/env python
# encoding: utf-8
'''
@author: Pan
@software: PyCharm
@file: server.py
@time: 2019/3/18 11:25
@desc:
'''

from socket import *
import time

'''
绑定ip端口，并等待一个连接
'''
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)

print ("The server is ready to receive")

'''
等待连接后发送接受到的数据以及当前时间给client
'''
while True:
    connectionSocket, addr = serverSocket.accept()
    curtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = 'receive: '+sentence +' at '+curtime
    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()
