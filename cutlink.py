import sys
import os
import glob
import pandas as pd
import time
import datetime
#def  getTime(day,month,year):# hàm lấy ngày tháng năm cần lấy logfile
    #time = datetime.date(year,month,day)
    #return time
def splitString(link):# nhập đường dẫn tới log file
    linkreplace =link.replace('/','//')
    return linkreplace
def joinLink(link):# joink vào đường dẫn và lấy tất cả đường dẫn của log file.
    return glob.glob(link)
def openFileCsv(link):
    read = pd.read_(link,encoding ='utf-8',header =None,index_col=None)


link = splitString("/home/tungkthd01/Documents/server.txt")
print(openFileCsv(link))