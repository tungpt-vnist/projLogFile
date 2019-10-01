def writeFile(linkfile,content):#ghi noi dung file log ra file khac
    with open(linkfile,mode="w+") as filecsv:
        filecsv.write(content)
def openLogFile(linkfile,linksavefile):# mo file log de ghi
    with open(linkfile) as filecsv:
        f=filecsv.read()
        writeFile(linksavefile,f)
writeFile("/var/log/cups/access_log","/home/tungkthd01/coypLogfile/access_log")