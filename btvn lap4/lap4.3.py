n = int(input("Nhập vào một số nguyên: "))
c = 0
if n == 0:
    c = 1
else:
    while n != 0:
        c += 1
        n //= 10
print("Số chữ số của số nguyên:", c)
