#!/usr/bin/python3

import socket
import time

#Multicast address and port have to match with cameralisten.py on other units
MCAST_ADDR = "225.1.1.1"
MCAST_PORT = 5007
TOKEN = "image2acgd" #Has to be identical for all desired camera units
MULTICAST_TTL = 2 #how many hops for packets

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
projectname = time.strftime('%Y%m%d-%H%M%S', time.localtime())
message = TOKEN + "_" + projectname
sock.sendto(message.encode("utf-8"), (MCAST_ADDR, MCAST_PORT))
sock.close()