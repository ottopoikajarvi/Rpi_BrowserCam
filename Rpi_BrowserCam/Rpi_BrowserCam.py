#!/usr/bin/python3

import subprocess

def takemcastpic():
    subprocess.Popen(["python3", "takeimagecmd.py"])

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
streamserver = start_streamserver()
sdserver = start_servicediscovery_server()
sdclient = start_servicediscovery_client()