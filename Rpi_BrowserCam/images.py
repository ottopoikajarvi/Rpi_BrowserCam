#!/usr/bin/python3

import cgi
import os


def showimages(imgdirectory):
    for item in imgdirectory:
        if item.endswith(".jpg"):
            itemname = item.split(".")
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
            """ % (item))

print("Content-Type: text/html")
print()
print("""
<html>
    <head>
        <title>RPi images</title>
    </head>
    <body>
""")

imgdirectory = os.listdir("/var/www")

showimages(imgdirectory)

print("""
    <body>
<html>
""")