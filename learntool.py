import glob
import os
def joinLink(link):# joink vào đường dẫn và lấy tất cả đường dẫn của log file.
    return (glob.glob(link))
a=[]
e=[]
b=joinLink("/var/log/*")
for c in b:
    if os.path.isdir(c):
        d=joinLink(c)
        a.append(d)
        #print(d)
    else:
        a.append(c)
        #print(c)
for i in a:
    print(i)
    if i == "*.log":
        e.append(i)

for i in e:
    print(i)