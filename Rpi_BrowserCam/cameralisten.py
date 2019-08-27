#!/usr/bin/python3

import socket
import struct
import subprocess
import time

#Multicast address and port have to match with takeimagecmd.py on other units
MCAST_ADDR = "225.1.1.1"
MCAST_PORT = 5007
TOKENCAMERA = "image2acgd" #Has to be identical for all units

def listen_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((MCAST_ADDR, MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_ADDR), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    return sock

sock = listen_socket()

while True:
    data = sock.recv(10240)
    data = data.decode("utf-8")
    if data.startswith(TOKENCAMERA):
        projectname = time.strftime('%Y%m%d%H%M%S', time.localtime())
        cmd = "raspistill -o /var/www/html/%s.jpg" % projectname
        pid = subprocess.run(cmd, shell=True)