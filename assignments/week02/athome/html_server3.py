#!/usr/bin/env python

import socket 
import email
import time


host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once
CLRF = "\r\n"#blank line
AllowedProtocal = ['HTTP/1.0','HTTP/1.1']
allowedMethods = ['GET']


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
    DateHeader = "date : "+email.Utils.formatdate(time.time())
    msg = header1+CLRF+DateHeader+CLRF+CLRF+body
    return msg

def client_error_response(error):
    DateHeader = "date : "+email.Utils.formatdate(time.time())
    if str(error) == 'NotAcceptable':
        return ("HTTP/1.1 406 Not Acceptable"+CLRF+DateHeader+CLRF+CLRF)
    else :
        return ("HTTP/1.1 400 Bad Request"+CLRF+DateHeader+CLRF+CLRF)

def parse_response(response):
    response_Line_list = response.split(CLRF)
    initial_line, headers = response.split('\r\n', 1)
    initial_line_split = initial_line.split()
    Method = initial_line_split[0]
    resource = initial_line_split[1]
    protocal = initial_line_split[2]
    try:
        if Method not in allowedMethods:
            raise NameError,'NotAcceptable'
        else :
            print " resource requested = "+ resource
            msg = ok_response(resource)
        
    
    except NameError,e:
        msg = client_error_response(e)
        
    
    return msg



while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    response = parse_response(data)
    if data: # if the connection was closed there would be no data
        print "sending back response %s"%response
        client.send(response) 
        client.close()
        


    