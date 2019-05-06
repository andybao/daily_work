#!/usr/bin/python

import socket, syslog, time
from blinkstick import blinkstick

IP = '192.168.3.252'
PORT = 6666

def process_user_commands():

    working_flag = True

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((IP, PORT))

    while working_flag:
        data = sock.recvfrom(1024)
        syslog.syslog(syslog.LOG_CRIT, 'chainvu_test data: {0}'.format(data))

        command = data[0]

        if (command=='led'):
            led = blinkstick.find_first()
            led.set_color(name='red')
            working_flag = False

if __name__ == '__main__':
    process_user_commands()