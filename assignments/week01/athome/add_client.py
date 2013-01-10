import socket
import sys
"""
client for add_server.py
send atlest 2 arguments with when invoking this script
"""
# Create a TCP/IP socket
client = socket.socket()

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)
client.connect(server_address)
messge_to_send = ''

try:
    # Send data
    ignorefirstArg = 1
    for args in sys.argv:# loop through the arguments, and send them to server        
        if ignorefirstArg != 1 :     #Don't send first argument it is name of the python script
            messge_to_send += args+" "
        ignorefirstArg +=1

    client.sendall(messge_to_send)

    # print the response
    msg_recieved = client.recv(4096)
    print msg_recieved

finally:
    # close the socket to clean up
    client.close()
