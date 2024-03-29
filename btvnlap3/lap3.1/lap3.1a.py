#bai1a
n = int(input("nhap n :"))
tong=0
if n >= 0:
    for i in range(1, n+1):
        tong += i
        if i < n:
            continue
    print("S1=",tong)
else:
    print("Vui lòng nhập lại số nguyên dương.")


