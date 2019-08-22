import paramiko, time, asyncio
from contextlib import contextmanager
host = '192.168.10.143'
username = 'pi'
password = '54bef519'

async def tcpdump():

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    try:
        print ("creating connection")
        ssh.connect(host, username=username, password=password)
        print ("connected")

        stdin, stdout, stderr = ssh.exec_command("sudo timeout 30 tcpdump -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'")
        # stdin, stdout, stderr = ssh.exec_command("/home/pi/bb/chainvu_ap/andy_function_1.sh")
        await function_1()
        for line in stdout:
            print('... ' + line.strip('\n'))

    finally:
        print ("closing connection")
        ssh.close()
        print ("closed")

async def function_1():

    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print ("creating connection")
        ssh1.connect(host, username=username, password=password)
        print ("connected")

        stdin, stdout, stderr = ssh1.exec_command("/home/pi/bb/chainvu_ap/andy_function_1.sh")
        for line in stdout:
            print('... ' + line.strip('\n'))

    finally:
        print ("closing connection")
        ssh1.close()
        print ("closed")

asyncio.run(tcpdump())