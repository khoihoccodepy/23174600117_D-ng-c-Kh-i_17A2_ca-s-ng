
n = int(input("Nhập số lượng phần tử trong mảng: "))
a = [0] * n
print("Nhập các phần tử của mảng:")
for i in range(n):
    a[i] = int(input())
e = 0
o = 0
for m in a:
    if m % 2 == 0:
        e += m
    else:
        o += m
print("Tổng các số chẵn trong mảng là:", e)
print("Tổng các số lẻ trong mảng là:", o)
