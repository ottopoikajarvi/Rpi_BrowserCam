#!/usr/bin/python3

import subprocess
import time


def start_piclisten():
    listenserver = subprocess.Popen(["python3", "cameralisten.py"])
    return listenserver

def start_streamserver():
    streamserver = subprocess.Popen(["python3", "cameraserver.py"])
    return streamserver

def start_servicediscovery_server():
    sdserver = subprocess.Popen(["python3", "servicediscovery_server.py"])
    return sdserver

def start_servicediscovery_client():
    sdclient = subprocess.Popen(["python3", "servicediscovery_client.py"])
    return sdclient

listenserver = start_piclisten()
time.sleep(0.5)
#streamserver = start_streamserver() disabled for comp issues
time.sleep(0.5)
sdserver = start_servicediscovery_server()
time.sleep(0.5)
sdclient = start_servicediscovery_client()
time.sleep(10)

while True:
    listenpoll = listenserver.poll()
    if listenpoll != None:
        listenserver = start_piclisten()
    #streampoll = streamserver.poll()
    #if streampoll != None:
        #streamserver = start_streamserver()
    sdserverpoll = sdserver.poll()
    if sdserverpoll != None:
        sdserver = start_servicediscovery_server()
    sdclientpoll = sdclient.poll()
    if listenpoll != None:
        sdclient = start_servicediscovery_client()
    time.sleep(30)
    print("Checking subprocess status...")