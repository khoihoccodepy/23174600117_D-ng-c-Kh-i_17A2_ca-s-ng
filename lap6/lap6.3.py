
n = input("Nhập dãy số: ").split()
n = [float(i) for i in n]
m= n[0]
p= n[0]
for i in n:
    if i > m:
        m = i
    if i< p:
       p = i
print("Số lớn nhất trong dãy số là:", m)
print("Số nhỏ nhất trong dãy số là:", p)
