import socket

def change_led_to_red():

    IP = '192.168.3.252'
    PORT = 6666

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    command = 'led'
    sock.sendto('{0}'.format(command).encode(),(IP, PORT))

if __name__ == "__main__":
    change_led_to_red()