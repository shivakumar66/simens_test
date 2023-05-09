from bluepy.btle import Peripheral, Characteristic, Service, UUID
import psutil

# Define the UUIDs for the battery service and characteristic
BATTERY_SERVICE_UUID = UUID("0000180f-0000-1000-8000-00805f9b34fb")
BATTERY_CHAR_UUID = UUID("00002a19-0000-1000-8000-00805f9b34fb")

# Define a BatteryService class that inherits from the bluepy Service class
class BatteryService(Service):
    def __init__(self, periph):
        # Call the parent constructor to initialize the service
        Service.__init__(self, periph, BATTERY_SERVICE_UUID, True)
        
        # Add a characteristic to the service for the battery level
        self.battery_char = Characteristic(self, BATTERY_CHAR_UUID, 
                                            properties=Characteristic.PROP_READ,
                                            value=0)

    def update_battery_level(self):
        # Get the current battery level from the system
        battery_level = psutil.sensors_battery().percent
        
        # Update the value of the battery characteristic with the new level
        self.battery_char.write(bytes([battery_level]), True)


# Create a BLE peripheral device and add the battery service to it
peripheral = Peripheral()
battery_service = BatteryService(peripheral)

# Set the name of the peripheral device to "Pc Battery"
peripheral.setLocalName("Pc Battery")

# Advertise the peripheral and its services every 200ms
peripheral.setAdvertisingInterval(200)
advertising_data = peripheral.getScanData()
advertising_data += peripheral.getServiceData()
peripheral.startAdvertising(advertising_data)

# Handle connections from the mobile app and update the battery level characteristic
while True:
    if peripheral.waitForConnections(1.0):
        # Connected to a central device
        battery_service.update_battery_level()
    else:
        # No connections, continue advertising
        peripheral.startAdvertising(advertising_data)
