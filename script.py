import nmap
import winsound
import time

# Replace with your MAC addresses
mac_addresses_to_watch = ["74:60:FA:12:17:45"]

# Function to play a sound
def play_sound():
    frequency = 3000  # Set the frequency (in Hz)
    duration = 1000  # Set the duration (in milliseconds)
    winsound.Beep(frequency, duration)

# Function to scan the network
def scan_network():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.3.0/24', arguments='-sn')

    detected = False  # Flag to track detection

    for host in nm.all_hosts():
        try:
            host_mac = nm[host]['addresses']['mac']
            if host_mac in mac_addresses_to_watch:
                print(f"Detected MAC address: {host_mac}, IP address: {host}")
                detected = True
        except KeyError:
            pass  # MAC address not found

    if detected:
        play_sound()

# Function to start monitoring
def start_monitoring():
    try:
        while True:
            scan_network()
            time.sleep(1)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("Monitoring stopped.")

# This code is now organized into functions for better readability.

if __name__ == "__main__":
    start_monitoring()