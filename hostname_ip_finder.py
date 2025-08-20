# HOSTNAME AND IP ADDRESS FINDER

# This proyect aims to find the hostname and IP address of a device

# Import necessary library to know the device's hostname and IP address
import socket

# Get and print the hostname of the device
hostname = socket.gethostname()
print("The hostname of the device is:", hostname)

# Get and print the IP address of the device
ip_address = socket.gethostbyname(hostname)
print("The IP Address of the device is:", ip_address)
