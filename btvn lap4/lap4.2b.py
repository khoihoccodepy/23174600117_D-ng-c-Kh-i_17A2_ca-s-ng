n= 1
print("Các số chính phương < 100 là:")
while n < 100:
    if n**0.5 == int(n**0.5):
        print(n, end=" ")
    n += 1