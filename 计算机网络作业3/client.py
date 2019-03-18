#!/usr/bin/env python
# encoding: utf-8
'''
@author: Pan
@software: PyCharm
@file: client.py
@time: 2019/3/18 11:25
@desc:
'''
from socket import *

'''
建立连接
'''
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

'''
发送数据
'''
sentence = input("input lowercase sentence:")
clientSocket.send(sentence.encode())

'''
接收server返回的数据
'''
modifiedSentence = clientSocket.recv(1024)
print("From Server:", modifiedSentence.decode())

clientSocket.close()

