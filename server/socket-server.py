#!/usr/bin/env python

import socket
import random


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

maxroll=20
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    myroll = random.randrange(1,maxroll)
    win = 0
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    if (int(data) > maxroll):
        win=127
    elif (int(data) < myroll):
        win=1
    if (win > 1):
        results = "You cheating bastard"
    else:
        results = "My roll was %s, yours was %s" % (myroll, data)
    #print "received data:", data
    conn.send(str(win))
    #conn.send(results)
    #conn.send(data)  # echo
#conn.close()
