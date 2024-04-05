import math

while True:
    n1 = float(input("Nhập số thứ nhất: "))
    n2 = float(input("Nhập số thứ hai: "))
    
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Lũy thừa")
    print("6. Căn bậc hai")
    
    c = int(input("Chọn phép tính (1-6): "))
    
    if c == 1:
        i = n1 + n2
        print("Kết quả của", n1, "+", n2, "là:", i)
    elif c == 2:
        i = n1 - n2
        print("Kết quả của", n1, "-", n2, "là:", i)
    elif c == 3:
        i = n1 * n2
        print("Kết quả của", n1, "*", n2, "là:", i)
    elif c == 4:
        if n2 != 0:
            i = n1 / n2
            print("Kết quả của", n1, "/", n2, "là:", i)
        else:
            print("Lỗi.")
    elif c == 5:
        i = n1 ** n2
        print("Kết quả của", n1, "^", n2, "là:", i)
    elif c == 6:
        if n2 >= 0:
            r = math.sqrt(n2)
            print("Căn bậc hai của", n2, "là:", r)
        else:
            print("Lỗi")
    else:
        print("Lỗi.")
        
    continue_choice = input("tiếp tục không? (c/k): ")
    if continue_choice.lower() != 'c':
        break
# bài này quá trời khó cô ơi=>
