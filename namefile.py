def nameFile(string):
    a=[]
    a=string.split("/")
    return a
tung="tung/pro/deche/aaa"
a=tung.split("/")
l=len(a)
print(a[l-1])
def writeFile(linkfile,content):#ghi noi dung file log ra file khac
    with open(linkfile,mode="w+") as filecsv:
        filecsv.write(content)
    filecsv.close()
def openLogFile(linkfile,linksavefile):# mo file log de ghi
    with open(linkfile) as filecsv:
        f=filecsv.read()
        writeFile(linksavefile,f)
    filecsv.close()

openLogFile()