import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

flag = True

while flag:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it

        data = connection.recv(16)

        if (data):
            print('received {!r}'.format(data))
            flag = False
        
        '''
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            flag = False
            
            if data:
                print('sending data back to the client')
                connection.sendall(data)
                #connection.close()
            else:
                print('no data from', client_address)
                break'''
    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()