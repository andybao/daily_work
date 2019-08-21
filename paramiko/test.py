import paramiko, time
from contextlib import contextmanager
from datetime import datetime

host = '192.168.10.143'
username = 'pi'
password = '54bef519'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

actual_services = []

try:
    print ("creating connection")
    ssh.connect(host, username=username, password=password)
    print ("connected")

    
    stdin, stdout, stderr = ssh.exec_command('ps aux | grep python')

    for line in stdout:
        actual_services.append(line.strip('\n'))
        # print('... ' + line.strip('\n'))


finally:
    print ("closing connection")
    ssh.close()
    print ("closed")

chainvu_services = [
    'startup_supervisor',
    'log_AP_Info',
    'blinkstick_driver',
    'forward_to_server',
    'demo_manager_client',
    'stray_pallet',
    'center_of_gravity',
    'ap_main',
    'rfid_gate_process'
]

chainvu_services.extend(['demo_manager_server.py','barcode_scanner_process.py'])

temp_services = chainvu_services.copy()

a = temp_services.copy()



for service in chainvu_services:
    for item in actual_services:
        if (service in item):
            temp_services.remove(service)
            break

print (temp_services)