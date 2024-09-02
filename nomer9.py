#cara mencari luas halaman
panjang_halaman = int(input("masukkan panjang halaman: "))
lebar_halaman = int(input("masukkan lebar halaman: "))

#rumus menghitung lebar halaman
halaman = panjang_halaman * lebar_halaman

#cara mencari luas rumah
panjang_rumah = int(input("masukkan panjang rumah: "))
lebar_rumah = int(input("masukkan lebar rumah: "))

#rumus mencari luas rumah
rumah = panjang_rumah * lebar_rumah

#mencari luas taman
taman = halaman - rumah

if taman <= 0:
    print("rumah tidak memiliki rumput yang bisa dipotong")
else:
    print(f"waktu pemotongan rumput selama {taman/2} detik ")
