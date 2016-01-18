# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:14:13 2016

@author: Anupam Srivastava
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.pythonlearn.com', 80))
sock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = sock.recv(512)
    if ( len(data) < 1 ):
        break
    print data;

sock.close()