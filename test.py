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
    a=[]
    with open(link,encoding="utf-8") as csv_file:
        for line in csv_file:
            line =  csv_file.readline()
            line1 = line.replace(" ",",")
            a.append(line1)
            writeFileCsv("/home/tungkthd01/Documents/test.csv",)
    return a
def writeFileCsv(linkFile,text):
    with open(linkFile,encoding="utf-8",mode='w') as csv_file:
        csv_file.writelines(text)

link = splitString("/home/tungkthd01/Documents/server.txt")
print(openFileCsv(link))
