#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import datetime
import socket

server_addr = socket.gethostbyname(socket.gethostname())


print "Content-Type: text/html"
print

body = """<html>
<head>
<title>Lab 1 - CGI experiments</title>
</head>
<body>
The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
The server address is %s:%s.<br>
<br>
Your hostname is %s.  <br>
<br>
You are coming from  %s:%s.<br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>

</body>
</html>""" % (
        os.environ['SERVER_NAME'], # Server Hostname
        server_addr, # server IP
        os.environ.get('SERVER_PORT', 'SERVER PORT NOT AVALIABLE'), # server port
        os.environ.get('REMOTE_HOST', 'CLIENT HOST NOT AVALIABLE'), # client hostname
        os.environ.get('REMOTE_ADDR', 'CLIENT IP NOT AVALIABLE'), # client IP
        os.environ.get('REMOTE_PORT', 'CLIENT PORT NOT AVALIABLE'), # client port
        os.environ.get('SCRIPT_NAME', 'SCRIPT NOT AVALIABLE'), # this script name
        datetime.datetime.now(), # time
        )

print body,
