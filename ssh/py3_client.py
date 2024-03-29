#!/usr/bin/env python3

import socket

HOST = '192.168.3.252'  # The server's hostname or IP address
PORT = 6666        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    command = 'led'
    s.sendall('{0}'.format(command).encode())
    # s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))