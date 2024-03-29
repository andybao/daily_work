import serial

class SerialWrapper:
    def __init__(self, device):
        self.ser = serial.Serial(device, 115200)

    def sendData(self, data):
        data += "\r\n"
        self.ser.write(data.encode())

def main():
    ser = SerialWrapper('/dev/tty.usbmodemL11003001')
    data = 'a'
    ser.sendData(data)