import asyncio
from bleak import BleakScanner, BleakClient

async def scan_and_pair():
    # Scan for nearby devices
    devices = await BleakScanner.discover()
    
    # Print out the list of discovered devices
    print("Discovered devices:")
    for device in devices:
        print(device)

    # Ask user to input the MAC address of the device to pair
    device_mac = input("Enter the MAC address of the device you want to pair: ")
    
    # Connect to the device
    client = BleakClient(device_mac)
    await client.connect()

    # Perform pairing process here, if needed
    # Depending on the device, you may need to perform specific pairing procedures.
    # This could involve exchanging PINs, passkeys, or other authentication mechanisms.

    # Once paired, you can perform further operations with the device.
    # For example, you can read/write characteristics, subscribe to notifications, etc.
    # Refer to Bleak documentation for more details on interacting with devices.

    # Disconnect from the device after pairing
    await client.disconnect()

# Run the main function
asyncio.run(scan_and_pair())
