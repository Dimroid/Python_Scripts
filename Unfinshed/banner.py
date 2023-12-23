import socket
import optparse
from threading import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)


parser = optparse.OptionParser("Help: " + "-H <tgtHost>, -P <tgtPort>")
parser.add_option("-H", dest="tgtHost", type="string", help="specify target")
parser.add_option("-P", dest="tgtPort", type="string", help="specify target" )
(options, args) = parser.parse_args()
tgtHost=options.tgtHost
tgtPorts=str(options.tgtPort).split(",")


def connScan(tgtHost, tgtPorts):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect_ex((str(tgtHost), int(tgtPorts)))
        print ("[+] Port %d is opened" %tgtPorts)
        s.close()
    except KeyboardInterrupt:
        print ("\n[+] You entered Ctrl + C")
    except:
        print ("[-] Port %d is closed" %tgtPorts)

def main():
    #running the Port scanner
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

if (tgtHost == None) | (tgtPorts[0] == None):
    print (parser.usage)
    exit(0)

if __name__ == "__main__":
    main()


