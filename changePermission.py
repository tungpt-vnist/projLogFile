import subprocess
import os
def startWithRoot(path,pass_sudo):
    if subprocess.check_output('whoami').strip()=='root':
        current_script = os.path.realpath(path)
        return os.system('echo %s| sudo chmod -R 444 %s' % (pass_sudo, current_script))
startWithRoot("/var/log/tallylog","tungkthd1234")