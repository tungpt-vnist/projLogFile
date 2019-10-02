import csv
import os
user={
    "name:":'',
    "userDate:":'',
    "Activity:":''
}
def getUser(string):
    c= string.replace('"',"'")
    a= c.split(" ",4)
    b=[]
    b.append(a[0])
    b.append(a[1])
    b.append(a[3])
    b.append(a[4])
    return b
def readFileSys(path):
    if os.path.isfile(path):
        with open(path,mode='r',encoding='utf-8') as file:
            read = file.readline()
            print(read)
            a=getUser(read)
            user["name:"]=a[2]
            date=a[1]+"-"+a[0]
            user["userDate:"]=date
            user["Activity:"]=a[3]
            user["name:"]='tung'

    else:
        return False
readFileSys("/home/tungkthd01/coypLogfile/syslog.1")
for x,y in user.items():
    print(x,y)
