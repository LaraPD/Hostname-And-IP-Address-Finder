# 🖥️ Hostname and IP Address Finder

This project finds the hostname and IP address of your device.  
It can be useful in cybersecurity, networking, or just to identify your machine in a network.

🌍 Available languages | [ESPAÑOL](README.es.md) 🔁 [ENGLISH](README.md) 

## ✨ Features
- Retrieves the hostname of the current device.
- Retrieves the main IP address of the current device.
- Easy to run and understand.

## 📚 Requirements
- Python 3.x
- No extra packages required (uses the built-in `socket` library).

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
- Useful as a building block for larger cybersecurity projects, such as network scanning and monitoring...

