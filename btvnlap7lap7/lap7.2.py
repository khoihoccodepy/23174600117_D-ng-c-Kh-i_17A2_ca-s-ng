
sv = {}
for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên thứ {i}: ")
    diem = float(input(f"Nhập điểm thi của sinh viên {ten}: "))
    sv[ten] = diem
tk = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for ten, diem in sv.items():
    if diem >= 8.5:
        tk['A'] += 1
    elif 7.0 <= diem < 8.5:
        tk['B'] += 1
    elif 5.5 <= diem < 7.0:
        tk['C'] += 1
    elif 4.0 <= diem < 5.5:
        tk['D'] += 1
    else:
        tk['F'] += 1
for loai, sl in tk.items():
    print(f"{loai}: {sl} sinh viên")
