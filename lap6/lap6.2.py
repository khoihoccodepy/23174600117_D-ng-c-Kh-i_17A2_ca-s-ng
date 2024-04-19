
n = int(input("Nhập số lượng phần tử trong mảng: "))
a= []
print("Nhập các phần tử của mảng:")
for i in range(n):
    a.append(int(input()))

print("Các số nguyên tố trong mảng là:")
for m in a:
    p = True
    if m > 1:
        for i in range(2, m):
            if m % i == 0:
                p = False
                break
        if p:
            print(m)
print("Các số hoàn hảo trong mảng là:")
for m in a:
    d = 0
    for i in range(1, m):
        if m % i == 0:
            d += i
    if d == m:
        print(m)

