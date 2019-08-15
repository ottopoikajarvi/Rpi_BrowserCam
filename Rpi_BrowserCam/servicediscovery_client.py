#!/usr/bin/python3

import socket

MCAST_ADDR = "224.1.1.1"
MCAST_PORT = 5008
TOKEN = "rpiservice" #Has to be identical for both client and server

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.sendto(TOKEN, (MCAST_GRP, MCAST_PORT))
sock.close()