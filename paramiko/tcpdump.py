import paramiko, time, datetime
from contextlib import contextmanager
host = '192.168.10.143'
username = 'pi'
password = '54bef519'

cmd_function_1 = '/home/pi/bb/chainvu_ap/andy_function_1.sh'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

a = []

try:
    print ("creating connection")
    ssh.connect(host, username=username, password=password)
    print ("connected")

    # stdin, stdout, stderr = ssh.exec_command("sudo timeout 30 tcpdump -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'")
    print (datetime.datetime.now())
    stdin, stdout, stderr = ssh.exec_command("sudo timeout 30 tcpdump -i wlan0 'port 443'")
    time.sleep(5)
    ssh.exec_command(cmd_function_1)
    i = 0 
    for line in stdout:
        print('... ' + line.strip('\n'))
        a.append(line)

finally:
    print ("closing connection")
    ssh.close()
    print ("closed")

print (len(a))
print (datetime.datetime.now())