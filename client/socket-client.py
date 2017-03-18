#!/usr/bin/env python

import socket
import random

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
maxroll=20
myroll = random.randrange(1,maxroll)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str(myroll))
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
