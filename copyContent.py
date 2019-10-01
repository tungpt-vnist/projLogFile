import csv
import re
import glob
import os
def permissionFile(linkfile):# thiết lập cấp quyền cho file.
    return os.chmod(linkfile,)
def nameFile(string):
    a=string.split("/")
    l=len(a)
    return a[l-1]
def joinLink(link):# joink vào đường dẫn và lấy tất cả đường dẫn của log file.
    return (glob.glob(link))
def writeFile(linkfile,content):#ghi noi dung file log ra file khac
    with open(linkfile,mode="w+") as filecsv:
        filecsv.write(content)
    filecsv.close()
def openLogFile(linkfile,linksavefile):
# mo file log de ghi voi linkfile là link mở file, linksavefile là link lưu copy
    with open(linkfile) as filecsv:
        f=filecsv.read()
        writeFile(linksavefile,f)
    filecsv.close()
def main():
    linkfilelog =joinLink("/var/log/*")
    linklog=[]
    filfile=[]
    namefile=[]
    linksave="/home/tungkthd01/coypLogfile"
    for link in linkfilelog:
        if os.path.isdir(link):
            link1=link+"/*"
            for link2 in link1:
                linklog.append(link2)
        else:
            linklog.append(link)
    for link in linklog:
        fil =re.search(r'.log$',link)
        if fil:
            filfile.append(link)
    for link in filfile:
        namefile.append(nameFile(link))
    for i in filfile:
        namefile =nameFile(i)
        linksavefile=linksave+"/"+namefile
        print(linksavefile)
        openLogFile(i,linksavefile)