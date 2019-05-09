import os, subprocess

cmd = 'cat ./led.py | ssh pi@192.168.3.252 sudo python -'
# os.system(cmd)

subprocess.Popen(cmd, shell=True)

'''
HOST = 'pi@192.168.3.252'

ssh = subprocess.Popen(['ssh ', HOST, 'uname -a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

results = ssh.stdout.readlines()

if results == []:
    print (ssh.stderr)
else:
    print (results)
'''