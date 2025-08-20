# 🖥️ Hostname and IP Address Finder

This project aims to find the hostname and IP address of a device. 
It can be useful in cybersecurity, networking, or just to identify your machine in a network.

🌍 Available languages | [ESPAÑOL](README.es.md) 🔁 [ENGLISH](README.md) 

## ✨ Features
- Get the hostname of the current device.
- Get the main IP address of the current device.
- Easy and simple to run and understand.

## 📚 Requirements
- Python 3.x
- No extra packages required. However, it may be necessary to install the *sockets* module using the command:
```bash
pip install sockets
```

## 🎯 Usage
Clone the repository and run the script from the terminal:

```bash
python hostname_ip_finder.py
```

## ✍️ Example
<img width="337" height="39" alt="image" src="https://github.com/user-attachments/assets/f1c2b60f-ec62-4012-ac2e-f164073b1ba5" />

## 📌 Recommendations
- This script only gives the primary IP.
- For all network interfaces consider using *psutil* or *netifaces*.
- Advanced options: Integrate with port scanning or export results to CSV/JSON for auditing.

