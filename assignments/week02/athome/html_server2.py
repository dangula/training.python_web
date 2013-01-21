#!/usr/bin/env python

import socket 
import email
import time


host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once
CLRF = "\r\n"#blank line


html = open('tiny_html.html','r').read()
## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 



def ok_response(body):
    header1 = "HTTP/1.1 200 OK"+CLRF
    header2 = "content-type : text/html"+CLRF
    header3 = "date : "+email.Utils.formatdate(time.time())+CLRF
    msg = header1+header2+header3+CLRF+CLRF+body
    return msg

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    if data: # if the connection was closed there would be no data
        print "received: %s, sending it back"%html
        client.send(ok_response(html)) 
        client.close()
        


    