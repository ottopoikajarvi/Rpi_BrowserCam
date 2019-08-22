#!/usr/bin/python3

import socket
import struct

#Multicast address and port have to match with servicediscovery_client.py on other units
MCAST_ADDR = "224.1.1.1"
MCAST_PORT = 5008
TOKEN = "rpiservice" #Has to be identical for both client and server
TOKEN_ANS = "answer" #Has to be identical for both client and server

def listen_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_ADDR), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    return sock

sock = listen_socket()

while True:
    data, client = sock.recvfrom(10240)
    data = data.decode("utf-8")
    print(data)
    print(client)
    if data.startswith(TOKEN):
        sock.sendto(TOKEN_ANS.encode("utf-8"), client)