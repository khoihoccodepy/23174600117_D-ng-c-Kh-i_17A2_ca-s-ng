x = float(input("nhap x: "))
y = float(input("nhap y: "))
z = float(input("nhap z: "))
if x>y and x<z or x<y and x>z:
    print("Ket qua : So lon thu hai la", x)
if y>x and y<z or y<x and y>z:
    print("Ket qua 1: So lon thu hai la", y)
if z>y and z<x or z<y and z>x:
    print("Ket qua 1: So lon thu hai la", z)
