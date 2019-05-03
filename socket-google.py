#!/usr/bin/python

import socket
import sys

def print_AP_Info():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    #print s.getsockname()
    print s

def main(argv):
    print_AP_Info()

if __name__ == "__main__":
    main(sys.argv[1:])