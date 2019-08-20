#!/usr/bin/python3

import cgi
import socket
import os

def takemcastpic():
    subprocess.run(["python3", "takeimagecmd.py"])

def get_rpi_ipaddr():
    testsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    testsock.connect(("8.8.8.8", 80))
    ipaddr = testsock.getsockname()[0]
    testsock.close()
    return ipaddr

def showimages(imgdirectory):
    for item in imgdirectory:
        if item.endswith(".jpg"):
            print("""
        <img src="/%s" width="400">
    </body>
</html>
""" % (item))

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
        <a href="%s:8000" target="_blank">Camera preview</a>
""" % (ipaddr, ipaddr))