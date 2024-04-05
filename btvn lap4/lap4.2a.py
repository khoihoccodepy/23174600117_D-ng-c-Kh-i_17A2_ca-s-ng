n = 2
print("Các số nguyên tố nhỏ hơn 100 là:")
while n < 100:
    i = True
    d= 2
    while d <= n // 2:
        if n % d == 0:
            i = False
            break
        d += 1
    if i:
        print(n, end=" ")
    n += 1