#!/usr/bin/python3

import subprocess

def takemcastpic():
    subprocess.Popen(["python3", "takeimagecmd.py"])

def startpiclisten():
    subprocess.Popen(["python3", "cameralisten.py"])

def startstreamserver():
    subprocess.Popen(["python3", "cameraserver.py"])