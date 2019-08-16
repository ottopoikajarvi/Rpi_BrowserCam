#!/usr/bin/python3

import socket
import struct

MCAST_ADDR = "224.1.1.1"
MCAST_PORT = 5008
TOKEN = "rpiservice" #Has to be identical for both client and server

def get_rpi_ipaddr():
    testsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    testsock.connect(("8.8.8.8", 80))
    ipaddr = testsock.getsockname()[0]
    testsock.close()
    return ipaddr

ipaddr = get_rpi_ipaddr()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((MCAST_ADDR, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_ADDR), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    data, client = sock.recvfrom(10240)
    print(data)
    print(client)
    #if data.startswith(TOKEN):
        #socket.sendto()