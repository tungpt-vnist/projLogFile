import subprocess
import re
import glob
import os
import getpass
def getUser():
    return getpass.getuser()

def permissionFile(path,pass_sudo):# thiết lập cấp quyền cho file.
    if subprocess.check_output('whoami').strip() != 'root':
        current_script = os.path.realpath(path)
        return os.system('echo %s| sudo -S chmod -R 444 %s' % (pass_sudo, current_script))
def nameFile(string):
    a=string.split("/")
    l=len(a)
    return a[l- 1]

def joinLink(link):                 # joink vào đường dẫn và lấy tất cả đường dẫn của log file.
    return (glob.glob(link))

def writeFile(linkfile,content):    #ghi noi dung file log ra file khac
    with open(linkfile,mode="w+") as filecsv:
        filecsv.write(content)
    filecsv.close()

def openLogFile(linkfile,linksavefile,info):# mo file log de ghi voi linkfile là link mở file, linksavefile là link lưu copy
    with open(linkfile,encoding='utf-8') as filecsv:
        f=filecsv.read()
        search ="r"+"'"+info+"'"
        find = re.search(r'%s'%info,f)
        #print(find.group())
        if find:
                writeFile(linksavefile,f)
        else:   
            s=input("file chua khong thong tin noi dung ve nguoi dung ban co muon copy hay khong,"
                    " co nhap y or yes,khong nhap no or n:")
            if s=="y" or s=="yes":
                writeFile(linksavefile,f)
            else:
                if s!= "y" or s!= "yes" or s!= "n" or s!= "no":
                    print("ban nhap sai cu phap,vui long nhap lai")
                    
                else:
                    False
    filecsv.close()

def main():
    user =getUser()
    linkfilelog =joinLink("/var/log/*") #lấy tât cả link trong thư mục log.
    linklog=[] # link của file log.
    filfile=[] # lọc link của file log chỉ có đuôi .log
    namefile=[] # tên của các file log trong thư mục copy.
    linksave="/home/tungkthd01/coypLogfile"
    for link in linkfilelog:
        if os.path.isdir(link):
            link1=link+"/*"
            link2 =joinLink(link1)
            for link3 in link2:
                linklog.append(link3)
        else:
            linklog.append(link)
    for link in linklog:
        fil =re.search(r'.log$',link)
        if fil:
            filfile.append(link)
    for link in filfile:
        print(link)
        namefile.append(nameFile(link))
    print(len(filfile))
    for i in filfile:
        namefile =nameFile(i)
        linksavefile=linksave+"/"+namefile
        print(i)
        permissionFile(i,'tungkthd1234')
        openLogFile(i,linksavefile,user)
if __name__ == '__main__':
    main()