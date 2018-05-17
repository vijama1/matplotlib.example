#!/usr/bin/python2

import  socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4>2:
    message=input("Enter your message: ")

    s.sendto(message.encode(),("127.0.0.1",10656))
