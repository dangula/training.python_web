#!/usr/bin/env python

import socket 
import email
import time
import os
import sys
from StringIO import StringIO




host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once
CRLF = "\r\n"#blank line
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
def construct_dirResponse(body):
    header1 = "HTTP/1.1 200 OK"
    dateHeader = "date : "+email.Utils.formatdate(time.time())
    contentHeader ="content-Type : text/html"
    msgContent = open(body+"/dirList.html",'r').read()
    msg = header1+CRLF+dateHeader+CRLF+contentHeader+CRLF+CRLF+msgContent
    return msg
    
def construct_fileResponse(body):
    header1 = "HTTP/1.1 200 OK"
    dateHeader = "date : "+email.Utils.formatdate(time.time())
    fileName = body.split("/")[-1]
    fileExt = fileName.split(".")[-1]
    if fileExt == 'txt':
        contentHeader ="content-Type : text/plain"
    elif fileExt == "html":
        contentHeader ="content-Type : text/html"
    elif fileExt == "jpeg":
        contentHeader ="content-Type : image/jpeg"
    elif fileExt == "png":
        contentHeader ="content-Type : image/png"
    else :
        contentHeader ="content-Type : text/plain"
    if fileExt == 'py':
        contentHeader ="content-Type : text/html"   
        
        buffer = StringIO()
        sys.stdout = buffer



        
        execCode = (execfile('web/'+fileName))

        msgContent = buffer.getvalue()        
        print msgContent
    else :
        msgContent = open(body,'r').read()
    
    msg = header1+CRLF+dateHeader+CRLF+contentHeader+CRLF+CRLF+msgContent
    return msg


    


def ok_response(body,type):
    if type == 'dir':
        msg = construct_dirResponse(body)
    if type == 'file':
        msg = construct_fileResponse(body)
    return msg

def client_error_response(error):
    DateHeader = "date : "+email.Utils.formatdate(time.time())
    if str(error) == 'NotAcceptable':
        return ("HTTP/1.1 406 Not Acceptable"+CRLF+DateHeader+CRLF+CRLF)
    elif str(error) == 'NotFound' :
        return("HTTP/1.1 404 Not FOUND"+CRLF+DateHeader+CRLF+CRLF)     
    else :
        return ("HTTP/1.1 400 Bad Request"+CRLF+DateHeader+CRLF+CRLF)

def parse_response(response):
    response_Line_list = response.split(CRLF)
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
            msg = resolve_uri(resource)
           
    except NameError,e:
        msg = client_error_response(e)
          
    return msg
def resolve_uri(resource):
    baseDir = 'web'
    currDir = baseDir+resource
    try:
        if os.path.isfile(currDir) :
            msg = ok_response(currDir,"file")

        elif os.path.isdir(currDir) :        
            msg = ok_response(currDir,"dir")
        else :
            raise ValueError,"NotFound"
        
    except ValueError,e:
        msg = client_error_response(e)
    
    return msg
        
while True: # keep looking for new connections forever
        client, address = s.accept() # look for a connection
        data = client.recv(size)
        response = parse_response(data)
        if data: # if the connection was closed there would be no data
            print "sending back response"
            client.send(response) 
            client.close()

        