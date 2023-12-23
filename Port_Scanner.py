#!/usr/bin/python3
#Created By Dimroid CEO
#you can show appreciation by sending gift card to his whatsapp Number +2348078595543


import socket
from threading import Thread
import optparse

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)

def connScan(IP, ports):
    try:
        s.connect((IP, ports))
        print("[+] Port %s is opened" %ports)
        s.close()
    except KeyboardInterrupt:
        print ("\nYou pressed Ctrl + C")
    except Exception as e:
        print ("[+] Port %s is closed" %ports)


def main():
    parser=optparse.OptionParser("Instructions: python3 Port_Scanner.py -H <IP> -P <Port>")
    parser.add_option("-H", dest="IP", type="string", help="specify the target IP")
    parser.add_option("-P", dest="port", type="string", help="specify target port, separate with commas if multiple")

#To call the variable out
    (options, args) = parser.parse_args()
    IP = options.IP
    port= options.port

#To print out instruction
    if (IP == None) | (port == None):
        print (parser.usage)
    else:
        for ports in port.split(","):
            t = Thread(target=connScan, args=(IP, int(ports)))
            t.start()

if __name__=="__main__":
    main()
