
#!/usr/bin/python3

import urllib.request as req
import cgi
import socket
import pickle
import os

LOCAL_PORT = 5134
TOKEN_LOC = "interrail"

def get_devices():
    intersock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    intersock.sendto(TOKEN_LOC.encode("utf-8"), ("127.0.0.1", LOCAL_PORT))
    devicesser, addr = intersock.recvfrom(10240)
    devicesfound = pickle.loads(devicesser)
    return devicesfound

imgdirectory = os.listdir("/var/www/html")


imageurl = "http://192.168.1.114/20190822163825.jpg"

req.urlretrieve(imageurl, "image_name.jpg")