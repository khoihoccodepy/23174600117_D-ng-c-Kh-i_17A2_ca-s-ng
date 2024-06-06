import random
ngua = {
    "Ngựa số 1": 0.2,
    "Ngựa số 2": 0.3,
    "Ngựa số 3": 0.1,
    "Ngựa số 4": 0.4,
    "Ngựa số 5": 0.25
}
vi_tri = {con_ngua: 0 for con_ngua in ngua}
while max(vi_tri.values()) < 500:
    for con_ngua, xac_suat in ngua.items():
        if random.random() < xac_suat:
            vi_tri[con_ngua] += 1  
vi_tri_cuoi_cung = sorted(vi_tri.items(), key=lambda x: x[1], reverse=True)
print("Kết quả:")
for con_ngua, khoang_cach in vi_tri_cuoi_cung:
    print(f"{con_ngua}: {khoang_cach} mét")

