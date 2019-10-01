import os
import subprocess
def permissionFile(path,pass_sudo):# thiết lập cấp quyền cho file.
    if subprocess.check_output('whoami').strip() == 'root':
        current_script = os.path.realpath(path)
        return os.system('echo %s| sudo chmod -R 444 %s' % (pass_sudo, current_script))
    else:
        return "ko thuoc root"
print(permissionFile("/var/log/tallylog","tungkthd1234"))