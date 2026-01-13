data = ["1","3","100","ukdc"]
elemen_cari = str(input("Masukkan elemen yang ingin dicari: "))

for i in range(len(data)):
    if elemen_cari == data[i]:
        print(f"data{elemen_cari} ditemukan di index {i}")
        break

else:
        print(f"data{elemen_cari} tidak ditemukan di data")

