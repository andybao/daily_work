import socket
from subprocess import Popen

cmd = 'node headless.js'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

p = Popen(cmd)

flag = True
finalData = ''

while flag:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it

        while flag:
            data = connection.recv(1024)
            if data:
                finalData = finalData + data.decode('utf-8')
                print (finalData)
                if (finalData.find('"Avengers"}') != -1):
                    flag = False

    finally:
        # Clean up the connection
        print("Closing current connection")
        p.terminate()
        connection.close()