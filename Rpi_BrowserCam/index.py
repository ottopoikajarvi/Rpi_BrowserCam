#!/usr/bin/python3

import cgi
import socket

def takemcastpic():
    subprocess.run(["python3", "sendcmd_os.py", "-o", "newimage.jpg"])

def get_rpi_ipaddr():
    testsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    testsock.connect(("8.8.8.8", 80))
    ipaddr = testsock.getsockname()[0]
    testsock.close()
    return ipaddr

ipaddr = get_rpi_ipaddr()

print("Content-Type: text/html")
print()
print("""
<html>
    <head>
        <title>RPi Camera control</title>
    </head>
    <body>
        <h1>Camera Control</h1>
        <p>If this is visible, the server is running</p>
        <p>This Raspberry Pi's local IP address is %s<p>
""" % (ipaddr))