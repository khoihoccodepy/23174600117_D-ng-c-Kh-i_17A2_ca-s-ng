t = 0
o = ""
e = ""
c = 0

while t<= 1000:
    n= int(input("Nhập một số nguyên dương: "))
    
    if n <= 0:
        print("Số phải là số nguyên dương. Vui lòng nhập lại.")
        continue
    
    t += n
    c += 1
    
    if n % 2 == 0:
        if e:
            e += " " + str(n)
        else:
            e += str(n)
    else:
        if o:
            o += " " + str(n)
        else:
            o += str(n)
print("Các số lẻ đã nhập là:", o)
print("Các số chẵn đã nhập là:", e)
print("Số lượng các số nguyên đã nhập:", c)
