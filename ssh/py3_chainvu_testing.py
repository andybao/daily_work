#!/usr/bin/python

import socket, syslog, time
from blinkstick import blinkstick

HOST = '192.168.3.252'
PORT = 6666

def process_user_commands():

    working_flag = True

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    # conn.sendall(b'empty command')
                    break
                syslog.syslog(syslog.LOG_CRIT, 'chainvu_test data: {0}'.format(data))
                command = data.decode("utf-8")
                if (command == 'led'):
                    led = blinkstick.find_first()
                    led.set_color(name = 'red')
                    #working_flag = False
                    #conn.sendall(b'done')
                    #conn.sendto(b'done', addr)
                else:
                    working_flag = True
                    # conn.sendall(b'invalid command')

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