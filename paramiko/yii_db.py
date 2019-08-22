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

    stdin, stdout, stderr = ssh.exec_command("/var/www/html/site_yii/tools/fix_its/clear_db.sh")

    for line in stdout:
        print('... ' + line.strip('\n'))

finally:
    print ("closing connection")
    ssh.close()
    print ("closed")