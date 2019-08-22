#!/usr/bin/python3

import socket

#Multicast address and port have to match with cameralisten.py on other units
MCAST_ADDR = "225.1.1.1"
MCAST_PORT = 5007
TOKEN = "image2acgd" #Has to be identical for all units
MULTICAST_TTL = 2 #how many hops for packets

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
sock.sendto(TOKEN.encode("utf-8"), (MCAST_ADDR, MCAST_PORT))
sock.close()