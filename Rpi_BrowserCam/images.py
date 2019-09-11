#!/usr/bin/python3

import cgi
import os
import subprocess
import socket

def get_rpi_ipaddr():
    testsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    testsock.connect(("8.8.8.8", 80))
    ipaddr = testsock.getsockname()[0]
    testsock.close()
    return ipaddr

#Iterates over images in directory, prints html for found images, including download links
def showimages(imgdirectory):
    ipaddr = get_rpi_ipaddr()
    imagenames = []
    for item in imgdirectory:
        if item.endswith(".jpg"):
            itemname = item.split(".")
            imagenames.append(itemname[0])
            print("""
        <img src="/%s" width="400">
            """ % (item))
            print("""
            <p>Image name: %s<p>
            """ % (itemname[0]))
            print("""
            <a href="/%s" download>
                Download this image
            </a>
            <br>
            """ % (ipaddr, item))
            print("""
            <form>
            <input type="submit" value="Retrieve all images of this set" name="%s" />
            <form><br>
            """ % (itemname[0]))
        elif item.endwith(".zip"):
            itemname = item.split(".")
            print("""
            <br>
            <p>Zip of images named %s<p>
            """ % (itemname[0]))
            print("""
            <a href="/%s" download>
                Download this zip
            </a>
            <br>
            """ % (ipaddr, item))
    return imagenames

form = cgi.FieldStorage()

print("Content-Type: text/html")
print()
print("""
<html>
    <head>
        <title>RPi images</title>
    </head>
    <body>
""")

imgdirectory = os.listdir("/var/www/html")

imagenames = showimages(imgdirectory)

print("""
    <body>
<html>
""")

if bool(form) == True:
    for name in imagenames:
        if name in form:
            subprocess.Popen(["/usr/bin/python3", "/var/www/html/multidload.py", name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)