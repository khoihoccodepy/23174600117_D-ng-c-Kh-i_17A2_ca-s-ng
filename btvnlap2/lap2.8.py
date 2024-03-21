a1 = float(input("nhap he so goc 1 :"))
b1 = float(input("nhap he so tu do 1 :"))
a2 = float(input("nhap he so goc 2 :"))
b2 = float(input("nhap he so tu do 2 :"))
if a1*a2 == -1:
    print("Hai duong thang vuông goc")
elif a1 != a2:
    print ("Hai duong thang cat nhau")
elif a1 == a2  and b1 != b2:
    print("Hai duong thang song song")
elif a1 == a2 and b1 == b2:
    print("Hai duong thang trung nhau")
else:
    print("")
    


