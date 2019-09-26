#ý tưởng : auto click file trong đường dẫn file log , đọc file và ghi dữ liệu ra file txt.
import datetime
def  getTime(day,month,year):
    time = datetime.date(year,month,day)
    return time
if __name__ == '__main__':
    x=int(input("nhap ngay:"))
    y=int(input("nhap thang:"))
    z=int(input("nhap nam:"))
    try:
        t=getTime(x,y,z)
        print(t)
    except NameError:
        print("ngay thang nam khong hop le")