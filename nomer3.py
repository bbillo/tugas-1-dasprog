#nomer 3

#mengubah waktu dalam bentuk jam dan menit menjadi bentuk desimal
jam = int(input('waktu dalam jam: '))
menit = int(input('waktu dalam menit: '))

#waktu dalam bentuk desimal
waktu_total = float(jam + (menit/60))

#mengitung temperatur
temperatur = float((4 * (waktu_total**2) / (waktu_total+2)) - 20)

#perkiraan temperatur
print(f"perkiraan suhu adalah {temperatur:.2f} °C")