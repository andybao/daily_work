#!/usr/bin/python

import socket, syslog, time
from blinkstick import blinkstick

HOST = '192.168.3.252'
PORT = 6666

def process_user_commands():

    working_flag = True

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while working_flag:
                data = conn.recv(1024)
                if not data:
                    break
                syslog.syslog(syslog.LOG_CRIT, 'chainvu_test data: {0}'.format(data))
                command = data.decode("utf-8")
                if (command == 'led'):
                    led = blinkstick.find_first()
                    led.set_color(name = 'red')
                    working_flag = False
                    conn.sendall(b'Done')

'''
        data = sock.recvfrom(1024)
        syslog.syslog(syslog.LOG_CRIT, 'chainvu_test data: {0}'.format(data))

        command = data[0]

        if (command=='led'):
            led = blinkstick.find_first()
            led.set_color(name='red')
            working_flag = False
'''

if __name__ == '__main__':
    process_user_commands()