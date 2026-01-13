amount = []
price = []
nama = []

print("Masukan barang belanja")

while True:
    print("Item barang ke")
    nama_barang = input("Masukan nama barang: ")
    harga_barang = float(input("Harga barang: "))
    jumlah_barang = int(input("Input jumlah barang: "))

    nama.append(nama_barang)
    price.append(harga_barang)
    amount.append(jumlah_barang)

    total_price = 0
    index = 0

    # Menghitung total harga tanpa menggunakan len() dan zip()
    while True:
        try:
            total_price += amount[index] * price[index]
            index += 1
        except IndexError:
            break
            
    print("Total harga: ", total_price)

    data = input("Apakah ingin menambahkan barang lain? (y/n): ")
    if data.lower() != "y":
        break

print("\nBelanja selesai!")
print("Daftar belanja:")

index = 0
# Menampilkan daftar belanja tanpa menggunakan len() dan zip()
while True:
    try:
        print(f"{nama[index]}: {amount[index]} x Rp{price[index]} = Rp{price[index] * amount[index]}")
        index += 1
    except IndexError:
        break

total_belanja = total_price 
print("Total belanja keseluruhan: ", total_belanja)

ppn = total_belanja * 0.10
total_belanja_dengan_ppn = total_belanja + ppn

print("Total belanja keseluruhan: ", total_belanja)
print("PPN 10%: ", ppn)
print("Total belanja setelah PPN: ", total_belanja_dengan_ppn)