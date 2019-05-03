import sys
from inspect import currentframe

import binascii
import socket
from subprocess import Popen

import datetime

def print_got_here():
    cf = currentframe()
    print ("Got to line {0} in andy_coord_simulator.py".format(cf.f_back.f_lineno))

def main(argv):
    process_coord_simulator_data()
    print_got_here()
    get_data_from_aws()

def get_data_from_aws():

    cmd = 'node headless.js'

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('Starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    p = Popen(cmd)

    flag = True
    finalData = ''

    while flag:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            # Receive the data in small chunks and retransmit it

            while flag:
                data = connection.recv(1024)
                if data:
                    finalData = finalData + data.decode('utf-8')
                    print (finalData)
                    if (finalData.find('"Avengers"}') != -1):
                        flag = False

        finally:
            # Clean up the connection
            print("Closing current connection")
            p.terminate()
            connection.close()

def process_coord_simulator_data():
    #aim_id = "8000000000000{0:03}".format(1)
    palletID = "pnubdmdv"
    aim_id = "00124b0006127618"
    nwk_addr = "8{0:03}".format(1)

    COORD_UDP_IP = "192.168.3.252"
    COORD_UPD_PORT = 5005

    coord_forward_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Connect pallet and aim using demo_manager_client.py
    '''
    command = "Pallet Association: "+palletID+" AimID: "+aim_id
    coord_forward_sock.sendto("<demomgr_msg msg_type=\"Server Command:\"><Command#>{0}</Command#></demomgr_msg>".format(command).encode(),(COORD_UDP_IP, 5559))
    '''

    #announcement_msg
    '''
    device_announcement_message = ("5A5A320011{0}{1}55AA".format(nwk_addr,aim_id))
    bin_msg = binascii.unhexlify(device_announcement_message.encode())
    print ("sending {0}".format(bin_msg))
    coord_forward_sock.sendto(bin_msg, (COORD_UDP_IP, COORD_UPD_PORT))
    '''

    #temperature_msg
    #asset_id = "Test0{0:03}".format(1)

    rssi_val = "3C"
    temp_val = "1190"
    temperature_message = ("5A5A01000C{0}{1}{2}55AA".format(nwk_addr,rssi_val,temp_val))
    print ("temperture_msg: {0}".format(temperature_message))
    bin_msg = binascii.unhexlify(temperature_message.encode())
    print ("sending {0}".format(bin_msg))
    print ("sending time: {0}".format(datetime.datetime.now()))
    coord_forward_sock.sendto(bin_msg, (COORD_UDP_IP, COORD_UPD_PORT))

if __name__ == "__main__":
   main(sys.argv[1:])