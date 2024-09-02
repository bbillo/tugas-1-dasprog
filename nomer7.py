#masukkan banyak minya 
galon_minyak = int(input("masukkan jumlah minyak: (dalam galon)"))

#mengubah satuan minyak
barel_minyak = galon_minyak/42

#menghitung BTU
btu = barel_minyak*5800000

print(f"{barel_minyak:.2f} barel minyak menghasilkan energi panas sebanyak {btu*0.65:2.2f} BTU")