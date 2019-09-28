import glob
import os
import re
def joinLink(link):# joink vào đường dẫn và lấy tất cả đường dẫn của log file.
    return (glob.glob(link))
a=[]
e=[]
b=joinLink("/var/log/*")
linklog=".log"
for c in b:
    if os.path.isdir(c):
        c1=c+"/*"
        d=joinLink(c1)
        for f in d:
            a.append(f)
    else:
        a.append(c)
for c in a:
    print(c)
    find =re.search(r'.log$',c)
    if find:
       e.append(c)
print("cac chuoi sau khi liet ke duoc:")
for i in e:
    print(i)

