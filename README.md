#BLE Peripheral to Publish Battery Level of PC

This project demonstrates how to use Python to create a BLE peripheral device that publishes the battery level of a PC over BLE. The peripheral device can be tested using the NRF Connect mobile app.

Requirements :
To run this project, you will need:

-> A PC running Windows, macOS, or Linux with Bluetooth LE support
-> Python 3.x installed on the PC
-> The bluepy Python library installed on the PC (pip install bluepy)
-> The psutil Python library installed on the PC (pip install psutil)
-> An NRF Connect mobile app installed on an Android or iOS device
Usage :
1.Clone this repository to your local machine.
2.Open a terminal or command prompt and navigate to the root directory of the cloned repository.
3.Run the ble_peripheral.py script using the command python ble_peripheral.py.
4.The peripheral device will advertise its services and name every 200ms.
5.Open the NRF Connect mobile app on your mobile device and tap the "Scan" button.
6.Wait for the BLE peripheral device named "Pc Battery" to appear in the list of nearby devices.
7.Tap on the name of the BLE peripheral device to connect to it.
8.Once connected, navigate to the "Services" tab in the NRF Connect app and locate the battery service and its battery level characteristic.
9.Tap on the battery level characteristic to read its value and view the current battery level of the PC.
