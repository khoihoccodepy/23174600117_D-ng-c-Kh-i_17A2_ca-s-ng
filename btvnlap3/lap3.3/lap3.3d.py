for i in range(1, 500):
    n = 0
    for j in range(1, i):
        if i % j == 0:
            n += j
    if n == i:
        print(i, end=" ")