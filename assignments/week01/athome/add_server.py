import socket

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
        msg = con.recv(4096)
        num_list = msg.split(); # Covert string recieved to list of strings(split by space)
        calc_sum =  int(num_list[0]) + int(num_list[1]) # calculate sum of first two strings
        returnMsg = "Sum of "+num_list[0]+" and "+num_list[1]+" is " + str(calc_sum) # return sum
        con.sendall(returnMsg)
           
    except ValueError :
        con.sendall("Error - please send 2 numbers")
    except IndexError :
        con.sendall("Error - please send 2 numbers")
    except :
        con.sendall("Oops!! Unexpected Error")
    
                
        
        
    finally:
        # Clean up the connection
        con.close
        

