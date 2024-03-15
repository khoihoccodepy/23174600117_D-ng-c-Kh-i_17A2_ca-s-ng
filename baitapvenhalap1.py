#bai1
print("""i carry your heart with me (i carry it in    
my heart) i am never without it (anywhere
i go you go, my dear; and whatever is done
by only me is your doing, my darling)
i fear no fate (for you are my fate, my sweet)
i want no world (for beautiful you are my world, my true)
and it's you are whatever a moon has always meant
and whatever a sun will always sing is you

here is the deepest secret nobody knows
(here is the root of the root and the bud of the bud
and the sky of the sky of a tree called life; which grows
higher than soul can hope or mind can hide)
and this is the wonder that's keeping the stars apart

i carry your heart (i carry it in my heart)
---i carry your heart with me by e.e. cummings---""")
#bai2
s = int(input("so luong sach :"))
m = int(input("Ma sach :"))
t = input("ten sach :")
tg = input("tac gia :")
nxb = int(input("nam xuat ban :"))
#bai3
t = float(input("nhap so tien ban gui :"))
n = float(input("nhap so nam ban gui tien :"))
amount = t + (0.06*t)*n
growth_rate = (amount - t)/ t
print("So tien ban nhan duoc sau ", n, "la :",round(amount, 2))
print("Ty le tang truong sau", n ,"nam la :", growth_rate)
#bai4
import math
h = float(input("nhap chieu cao :"))
a = float(input("nhap do dai canh :"))
p = 4*a
l = math.sqrt(h**2+(a/2)**2)
s = 1/2 * p * l
sd = ((a**2)*math.sqrt(3))/4
print("dien tich xung quanh cua hinh chop tu giac deu :", round(s, 2))
print("dien tich toan phan cua hinh chop tu giac deu :", round(sd+s, 2))
print("the tich cua hinh chop tu giac deu :", round(1/3 * sd * h, 2))
#bai5
t = float(input("nhap thoi gian su dung :"))
i = 1.5
u = 220
p = u*i
tien_dien = p * t * 5
print("tien dien ban phai tra la :", tien_dien)
#bai6 
a1, a2 = map(float, input("nhap toa do vecto a :").split())
b1, b2 = map(float, input("nhap toa do vecto b :").split())
cs = (a1*b1 + a2*b2)/(math.sqrt(a1**2 + a2**2)*math.sqrt(b1**2 + b2**2))
print("Tong hai vecto :", (a1+b1, a2+b2))
print("Hieu hai vecto :", (a1-b1, a2-b2))
print("do dai vecto A :", math.sqrt(a1**2 + a2**2))
print("do dai vecto B :", math.sqrt(b1**2 + b2**2))
print("Cosin góc hợp giữa hai vecto a và b la ", round(cs, 2))
#bai7
a1, b1, c1  = map(float, input("nhap a1 b1 c1 :").split())
a2, b2, c2  = map(float, input("nhap a2 b2 c2 :").split())
x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
print("Gia tri của x la:", round(x, 2))
print("Gia tri của y la:", round(y, 2))
#bai8
import math
x = float(input("nhap x :"))
z = float(input("nhap z :"))
f = ((x**2)*math.sin(z) + math.sqrt(abs(x))) / (math.log(z) + math.exp(x-1)) + math.atan(x*z)
print("f(x,y)= ", round(f, 2))
#bai9
m1, m2 = map(float, input("nhap toa do cua M :").split())
n1, n2 = map(float, input("nhap toa do cua N :").split())
p1, p2 = map(float, input("nhap toa do cua P :").split())
q1, q2 = map(float, input("nhap toa do cua Q :").split())
print("Toa do trung diem cua canh MN la : ", ((m1+n1)/2, (m2+n2)/2 ))
print("Toa do trung diem cua canh NP la : ", ((p1+n1)/2, (p2+n2)/2 ))
print("Toa do trung diem cua canh PQ la : ", ((p1+q1)/2, (p2+q2)/2 ))
print("Toa do trung diem cua canh QM la : ", ((m1+q1)/2, (m2+q2)/2 ))
#bai10
d = 20
x = 15
v = 15
t = d + x + v
n = int(input("nhap so bi ban muon rut :"))
print("Xac xuat tat ca deu la do :", (d/t))
#bai10 nay kho qua co ơi !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!