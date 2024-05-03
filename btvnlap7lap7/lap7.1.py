N = int(input("Nhập N: "))
t = {}

for x in range(1, N+1):
    t[x] = x ** 3

print("Từ điển dạng sinh viên:")
for k in t:
    print(f"{k}: {t[k]}")
