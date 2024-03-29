n = int(input("nhap n :"))
tong=0
if n >= 0:
    for i in range(1, n+1):
        tong += 1/i
        if i < n:
            continue
    print("S2=",tong)
else:
    print("Vui lòng nhập lại số nguyên dương.")