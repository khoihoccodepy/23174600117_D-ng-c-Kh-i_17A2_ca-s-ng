import math
r = float(input("Nhap ban kinh :"))
x, y = map(float, input("Nhap toa do tam duong tron :").split())
a = float(input("nhap he so goc a :"))
b = float(input("nhap he so goc b :"))
c = float(input("nhap he so tu do c :"))
d = abs(a*x+b*y+c)/math.sqrt((a**2)+(b**2))
if d == 0 :
    print("Duong thang tiếp xuc duong tron")
elif d>r :
    print("Duong thang nam ngoai duong tron")
else :
    print("Duong thang nam trong duong tron")
    
