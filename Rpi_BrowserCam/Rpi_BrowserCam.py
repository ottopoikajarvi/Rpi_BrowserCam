#This is the main file

import subprocess

def takemcastpic():
    subprocess.run(["python3", "sendcmd_os.py", "-o", "newimage.jpg"])

def startpiclisten():
    subprocess.run(["python3", "listen_os.py"])

def startstreamserver():
    subprocess.run(["python3", "cameraserver.py"])