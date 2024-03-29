tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
        if i == 1000:
            break
print("Tổng của tất cả các số thỏa mãn điều kiện là:", tong)   