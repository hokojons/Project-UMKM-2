pola = []
jumlah_koordinat = int(input("Masukkan jumlah koordinat: "))

for i in range(jumlah_koordinat):
    x = int(input(f"Masukkan x untuk koordinat : "))
    y = int(input(f"Masukkan y untuk koordinat : "))
    pola.append([x, y])

print("\nHasil Koordinat:")
for x, y in pola:
    print(f"({x}, {y})")