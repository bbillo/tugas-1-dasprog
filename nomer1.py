#nomer 1, menghitung biaya taxi

#menghitung jarak tempuh
odometer_awal = float(input("odometer awal: "))
odometer_akhir = float(input("odometer akhir: "))

jarak = (odometer_akhir-odometer_awal)

#menghitung tarif
tarif = jarak * 1.50

#tarif
print(f"kamu menempuh jarak sejauh {jarak:.2f}mil dan jumlah yang harus dibayar sebanyak ${tarif:.2f} ")

