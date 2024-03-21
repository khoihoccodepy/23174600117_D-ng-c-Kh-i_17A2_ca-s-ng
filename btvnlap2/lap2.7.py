h = float(input("Nhập chiều cao(m) :"))
w = float(input("Nhập cân nặng(kg) :"))
bmi = w/(h**2)
if bmi<18.5:
    print("Chỉ số BMI của bạn là:", bmi, "Gầy")
elif 18.5<=bmi<24.9:
    print("Chỉ số BMI của bạn là:", bmi, "Bình thường")
elif 24.9<= bmi<29.9:
    print("Chỉ số BMI của bạn là:", bmi, "Hơi béo")
elif 29.9<= bmi :
    print("Chỉ số BMI của bạn là:", bmi, "Béo")
