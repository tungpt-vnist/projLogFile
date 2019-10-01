import os,stat
import platform
import subprocess

#print(os.name)
#print(platform.system())
#print(platform.())
#print(os.chmod( '/home/tungkthd01/coypLogfilebootstrap.log', stat.S_IWUSR))
#print(subprocess.call(['chmod','0444','/home/tungkthd01/coypLogfiledpkg.log']))
pass_sudo = 'tungkthd1234'
def startWithRoot():
    if subprocess.check_output('whoami').strip()=='root':
        return True
    return False
#x=os.chmod("/var/log/tallylog", 0o774)
#subprocess.call(['sudo','python3']+os.chmod("/var/log/tallylog", 0o774))
def runningAsRoot():
    print("sucessfuly")
def main():
    if startWithRoot():
        print("ok, test will be good")
        runningAsRoot()
    else:
        print("this is a user")
        current_script= os.path.realpath(__file__)
        os.system('echo %s| sudo -S python %s' % (pass_sudo,current_script))
def isgroupreadable(filepath):
  st = os.stat(filepath)
  return bool(st.st_mode & stat.S_IRGRP)
if __name__ == '__main__':
    main()
    x = os.chmod("/var/log/tallylog", 0o774)