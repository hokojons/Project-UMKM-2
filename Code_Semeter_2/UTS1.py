print(".:Placeholder:.")
name = []
price = []
quantity = []

while True:
    name.append(input("Nama Barang: "))
    price.append(float(input("Harga: ")))
    quantity.append(int(input("Jumlah: ")))
    
    exit = input("Tambah lagi? (Y/N):  ")
    if exit.upper() == "N":
        break

data = {'Nama Barang': name, 'Harga': price, 'Jumlah': quantity}
total_price = sum(p * q for p, q in zip(price, quantity))

print("\nDaftar Belanjaan:")
for n, p, q in zip(name, price, quantity):
    print(f"{n}: {q} x Rp{p} = Rp{p * q}")

print(f"Total: Rp{total_price}")