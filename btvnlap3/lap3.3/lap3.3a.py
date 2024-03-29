for i in range(100, 1001):
    if i > 1:
        t = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                t = False
                break
        if t:
            print(i, end=" ")
