#/user/bin/python

import sys
from inspect import currentframe

import binascii
import socket



def print_got_here():
    cf = currentframe()
    print ("Got to line {0} in andy_coord_simulator.py".format(cf.f_back.f_lineno))

def main(argv):
    process_coord_simulator_data()
    print_got_here()

def process_coord_simulator_data():
    #aim_id = "8000000000000{0:03}".format(1)
    palletID = "pnubdmdv"
    aim_id = "00124b0006127618"
    nwk_addr = "8{0:03}".format(1)

    COORD_UDP_IP = "192.168.3.252"
    COORD_UPD_PORT = 5005

    coord_forward_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Connect pallet and aim using demo_manager_client.py

    command = "Pallet Association: "+palletID+" AimID: "+aim_id
    coord_forward_sock.sendto("<demomgr_msg msg_type=\"Server Command:\"><Command#>{0}</Command#></demomgr_msg>".format(command).encode(),(COORD_UDP_IP, 5559))


    #announcement_msg
    '''
    device_announcement_message = ("5A5A320011{0}{1}55AA".format(nwk_addr,aim_id))
    bin_msg = binascii.unhexlify(device_announcement_message.encode())
    print ("sending {0}".format(bin_msg))
    coord_forward_sock.sendto(bin_msg, (COORD_UDP_IP, COORD_UPD_PORT))
    '''

    #temperature_msg
    #asset_id = "Test0{0:03}".format(1)
    '''
    rssi_val = "3C"
    temp_val = "1190"
    temperature_message = ("5A5A01000C{0}{1}{2}55AA".format(nwk_addr,rssi_val,temp_val))
    bin_msg = binascii.unhexlify(temperature_message.encode())
    print ("sending {0}".format(bin_msg))
    coord_forward_sock.sendto(bin_msg, (COORD_UDP_IP, COORD_UPD_PORT))
    '''
if __name__ == "__main__":
   main(sys.argv[1:])