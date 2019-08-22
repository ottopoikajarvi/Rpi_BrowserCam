#!/usr/bin/python3

import cgi


def showimages(imgdirectory):
    for item in imgdirectory:
        if item.endswith(".jpg"):
            print("""
        <img src="/%s" width="400">
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