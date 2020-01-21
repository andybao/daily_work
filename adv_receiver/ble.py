import gatt

class AnyDeviceManager(gatt.DeviceManager):
    def device_discovered(self, device):
        if (device.mac_address == 'f0:f8:f2:d2:c0:2e'):
            print("[%s] Discovered, alias = %s" % (device.mac_address, device.alias()))

manager = AnyDeviceManager(adapter_name='hci0')
manager.start_discovery()