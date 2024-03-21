n = int(input("Nhập số lượng người :"))
x = 120000
if n == 1 :
    print("Giá vé là :", x, "VND")
elif 2<= n <4 :
    print("Giá vé là :", x*n - x*n*0.05, "VND")
elif 4<= n <10 :
    print("Gia ve la :", x*n - x*n*0.1, "VND")
elif n>= 10:
    print("Giá vé là :", x*n - x*n*0.2, "VND")
else:
    print("Không hợp lệ")