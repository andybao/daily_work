import os
from subprocess import Popen
from pathlib import Path
import socket

PROJECT_ROOT = Path().absolute()
FILE = os.path.join(PROJECT_ROOT, 'py3_chainvu_testing.py')

cmd = 'cd C:\Windows\System32\OpenSSH & cat ' + FILE + ' | ./ssh.exe pi@192.168.3.252 sudo ~/Testing/testingEnv/bin/python3 -'

# cmd = 'ssh pi@192.168.3.252 sudo ~/Testing/testingEnv/bin/python3 < ' + FILE

print (cmd)

Popen(['cmd', cmd], shell=True)

# Popen(cmd, shell=True)

'''

HOST = '192.168.3.252'  # The server's hostname or IP address
PORT = 6666        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    command = 'led'
    s.sendall('{0}'.format(command).encode())
    # s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
'''