
#!/usr/bin/python3
#Requires image name as argument

import urllib.request as req
import cgi
import socket
import pickle
import os
import sys
import shutil

LOCAL_PORT = 5134
TOKEN_LOC = "interrail"

if len(sys.argv) != 2:
    print("Incorrect arguments")
    sys.exit(1)

imgname = sys.argv[1]

def get_devices():
    intersock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    intersock.sendto(TOKEN_LOC.encode("utf-8"), ("127.0.0.1", LOCAL_PORT))
    devicesser, addr = intersock.recvfrom(10240)
    devicesfound = pickle.loads(devicesser)
    return devicesfound

imgdirectory = "/var/www/html/" + imgname
os.mkdir(imgdirectory)
devicesfound = get_devices()

#retrieve images
for device in devicesfound:
    deviceid = device.split(".")[3]
    imageurl = "http://%s/%s.jpg" % (device, imgname)
    jpgname = deviceid + ".jpg"
    jpgloc = imgdirectory + jpgname
    try:
        req.urlretrieve(imageurl, jpgloc)
    except:
        print("Image retrieval failed from: %s" % device)
        continue

#zip the folder
zipfolder = "/var/www/html/" + imgname
shutil.make_archive(zipfolder, "zip", imgdirectory)
shutil.rmtree(imgdirectory)