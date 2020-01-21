import paramiko, time
from contextlib import contextmanager
host = '192.168.10.143'
username = 'pi'
password = '54bef519'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
try:
    print ("creating connection")
    ssh.connect(host, username=username, password=password)
    print ("connected")

    i = 0
    j = 0

    stdin, stdout, stderr = ssh.exec_command("ps aux | grep python")
    for line in stdout:
        line = line.strip()
        if 'ble_discover.py' in line:
            i += 1
        if 'ble_process.py' in line:
            j += 1

finally:
    print ("closing connection")
    ssh.close()
    print ("closed")

print (i)
print (j)