import subprocess
import os
def startWithRoot(path,pass_sudo):
    s=' change for successful'
    if subprocess.check_output('whoami').strip()=='root':
        return True
    else:
        return os.system("echo %s| sudo chmod -R 444 %s" %(pass_sudo,path))
print(startWithRoot("/var/log/installer/casper.log","tungkthd1234"))