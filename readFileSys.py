import csv
import os
import json
class User:
    def __init__(self,name,userDate,activity):
        self.name = name
        self.userDate =userDate
        self.activity = activity
    def showUser(self):
        print(self.name)

useruse=[]
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
            i=1
            max = 0
            readline=file.read()
            userf = getUser(readline)
            date = userf[1]+"-"+userf[0]
            user1 =User(userf[2],date,userf[3])
            useruse.append(user1)
            #read = file.readline()
            #print(read)
            #a=getUser(read)
            #date = a[1] + "-" + a[0]
            #User1 =User(a[2],date,a[3])
            #User2 =User("tung","21/03","coder")
            #useruse.append(User1)
            #useruse.append(User2)
            for line in file:
                info = getUser(line)
                date1 = info[1]+'-'+info[0]
                user="user"+ str(i)
                user=User(info[2],date1,info[3])
                if user.name !=info[2]:
                    i = i + 1
                    user =User(info[2],date1,info[3])
                    useruse.append(user)
                max = max+1
                if(max==2000):
                    break

    else:
        return False
readFileSys("/home/tungkthd01/coypLogfile/syslog.1")
print(len(useruse))
for i in useruse:
    i.showUser()
