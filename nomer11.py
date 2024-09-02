#masukkan nilai m dan n, dimana m > n
m = int(input("masukkan nilai dari m: "))
n = int(input("masukkan nilai dari n: "))

#rumus
sisi1 = (m**2) - (n**2)
sisi2 = 2*m*n
sisi_miring = (m**2) + (n**2)

if m < n:
    print("sisi m harus lebih besar dari pada sisi n")
else:
    print(f'panjang dari sisi-sisi segitiga adalah {sisi1}, {sisi2}, dan {sisi_miring}')