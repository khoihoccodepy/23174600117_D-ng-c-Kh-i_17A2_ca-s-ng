
s = input("Nhập dãy số: ").split()
s = [int(n) for n in s]
d = [s[i] - s[i-1] for i in range(1, len(s))]
o = all(j == d[0] for j in d)
if o:
    print("Dãy số", s, "tạo thành cấp số cộng.")
else:
    print("Dãy số", s, "không tạo thành cấp số cộng.")

