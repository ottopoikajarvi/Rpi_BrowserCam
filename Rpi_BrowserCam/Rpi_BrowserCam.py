#!/usr/bin/python3
#This is the main file

import subprocess

def takemcastpic():
    subprocess.run(["python3", "takeimagecmd.py"])

def startpiclisten():
    subprocess.run(["python3", "cameralisten.py"])

def startstreamserver():
    subprocess.run(["python3", "cameraserver.py"])