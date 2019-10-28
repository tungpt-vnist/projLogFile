import copyusb
import glob
def joinLink(link):                 # joink vào đường dẫn và lấy tất cả đường dẫn của log file.
    return (glob.glob(link))
x= joinLink("/home/tungkthd01/coypLogfile/*")
for y in x:
    print(y)
    copyusb.copy_single_file(y,'/media/tungkthd01/UBUNTU 18_0')


