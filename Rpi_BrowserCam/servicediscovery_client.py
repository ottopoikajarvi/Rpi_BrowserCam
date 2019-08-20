#!/usr/bin/python3

import socket
import pickle

#Multicast address and port have to match with servicediscovery_client.py on other units
MCAST_ADDR = "224.1.1.1"
MCAST_PORT = 5008
LOCAL_PORT = 5134
TOKEN = "rpiservice" #Has to be identical for both client and server
TOKEN_ANS = "answer" #Has to be identical for both client and server
MULTICAST_TTL = 2 #how many hops for packets
devicesfound = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
sock.sendto(TOKEN.encode("utf-8"), (MCAST_ADDR, MCAST_PORT))

while True:
    sock.settimeout(1)
    try:
        data, server = sock.recvfrom(10240)
        data = data.decode("utf-8")
        #print(data)
        #print(server)
        if data.startswith(TOKEN_ANS):
            devicesfound.append(server[0])
    except socket.timeout:
        print("No more new devices found")
        print(devicesfound)
        sock.close()
        break

intersock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
intersock.bind(("127.0.0.1",LOCAL_PORT))

while True:
    data, client = intersock.recvfrom(10240)