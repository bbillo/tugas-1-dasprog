#jumlah cairan yang harus disuntikkan
cairan = int(input("masukkan jumlah cairan yang harus disuntikkan: (dalam ml) "))

#durasi cairan yang akan disutikkan
durasi = int(input("masukkan durasi penyuntikkan cairan: (dalam menit)"))

#durasi cairan yang akan disuntikkan dalam jam
durasi_jam = (cairan//durasi)*60

print(f"banyak cairan yang akan disuntikkan sebanyak {cairan}ml dengan laju infus {durasi_jam}ml/jam")