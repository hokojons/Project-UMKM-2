data=[]
while True:
    print("selamat datang di Toko UKDC")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tunjukan Data")
    print("4.Exit")

    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        data.append(input("masukan data: "))
        print(data)
    elif pilihan == "2":
        deldata = input("Hapus data: ")
        if  deldata in data:
            data.remove(deldata)
            print("Data berhasil dihapus:", data)
        else:
            print("Data tidak ditemukan.")
        print(data)
    elif pilihan =="3":
        print(data)
    elif pilihan =="4":
        break

    
