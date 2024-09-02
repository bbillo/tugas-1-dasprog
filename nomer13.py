#masukkan banyak siswa
siswa = int(input("masukkan jumlah siswa: "))

#pembagian kelompok
kelompok = siswa//30
sisa_siswa = siswa - (kelompok*30)

#jumlah kelompok
if sisa_siswa <= 0:
    print (f"jumlah kelompok yang akan terbentuk sebanyak {kelompok} kelompok dan semua siswa memiliki kelompok")
else:
    print(f"jumlah kelompok yang akan terbentuk sebanyak {kelompok} kelompok dan jumlah siswa yang tidak mendapatkan kelompok sebanyak {sisa_siswa} siswa")


