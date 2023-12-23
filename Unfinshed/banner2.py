#!/usr/bin/python3
#Created By Dimroid CEO
#you can show appreciation by sending gift card to his whatsapp Number +2348078595543


import socket
from threading import Thread
import optparse

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)
IP = input("Enter the website IP: ")
def connScan(IP, ports):
    try:
        s.connect((IP, ports))
        s.close()
        print("[+] Port %s is opened" %ports)
    except KeyboardInterrupt:
        print ("\nYou pressed Ctrl + C")
    except Exception as e:
        print ("[+] Port %s is closed due to" %ports)
        print (e)


def main():
#To print out instruction
        for ports in range(1,1001):
            t = Thread(target=connScan, args=(IP, int(ports)))
            t.start()

if __name__=="__main__":
    main()
