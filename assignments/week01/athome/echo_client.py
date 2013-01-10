import socket
import sys

# Create a TCP/IP socket
client = socket.socket()

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)
client.connect(server_address)

try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    client.sendall(message)

    # print the response
    msg_recieved = client.recv(4096)
    print msg_recieved

finally:
    # close the socket to clean up
    client.close()
