import socket
import sys

server = socket.socket()
# Bind the socket to the port
server_address = ('localhost', 50000)
server.bind(server_address)

# Listen for incoming connections
server.listen(10)

while True:
    # Wait for a connection
    con,addr = server.accept()

    try:
        # Receive the data and send it back
	msg = con.recv(4096)
	print msg
        con.sendall(msg)
        

    finally:
        # Clean up the connection
        con.close
        

