#!/usr/bin/python3

import cgi
import socket
import subprocess
import pickle

LOCAL_PORT = 5134
TOKEN_LOC = "interrail"

def takemcastpic():
    subprocess.run(["python3", "takeimagecmd.py"])

def get_rpi_ipaddr():
    testsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    testsock.connect(("8.8.8.8", 80))
    ipaddr = testsock.getsockname()[0]
    testsock.close()
    return ipaddr

def get_devices():
    intersock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    intersock.sendto(TOKEN_LOC.encode("utf-8"), ("127.0.0.1", LOCAL_PORT))
    devicesser, addr = sock.recvfrom(10240)
    devicesfound = pickle.loads(devicesser)
    return devicesfound

def show_devices(devicesfound):
    devicecount = len(devicesfound)
    print("""
    <p>The network has %d units</p>
    """ % (devicecount))
    for unit in devicesfound:
        print("""
        <p>%s<p>
        """ % (unit))
    return

def showimages(imgdirectory):
    for item in imgdirectory:
        if item.endswith(".jpg"):
            print("""
        <img src="/%s" width="400">
            """ % (item))

ipaddr = get_rpi_ipaddr()
devicesfound = get_devices()

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

show_devices(devicesfound)

print("""
    <body>
<html>
""")