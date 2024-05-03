kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don = {}
tong_tien = 0

for mat_hang in kho:
    so_luong = kho[mat_hang]
    if so_luong > 0:
        so_luong_mua = min(so_luong, 3)  
        thanh_tien = gia_tien[mat_hang] * so_luong_mua
        hoa_don[mat_hang] = {
            'Số lượng': so_luong_mua,
            'Đơn giá': gia_tien[mat_hang],
            'Số tiền': thanh_tien
        }
        tong_tien += thanh_tien
        kho[mat_hang] -= so_luong_mua

print("Hóa đơn mua hàng:")
for mat_hang in hoa_don:
    thong_tin = hoa_don[mat_hang]
    print(f"Mặt hàng: {mat_hang}, Số lượng: {thong_tin['Số lượng']}, Đơn giá: {thong_tin['Đơn giá']}, Số tiền: {thong_tin['Số tiền']}")

print(f"Tổng số tiền của hóa đơn: {tong_tien}")

print("\nSố lượng của các mặt hàng trong kho sau khi mua:")
print(kho)
