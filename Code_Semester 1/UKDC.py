data = []  

    
def function():  
    data.append(input("Masukan data: ")) 
    print (data)

def fuction2(): 
    data.remove(input("Masukan data yang ingin dihapus: "))  # Remove specified data
    print(data)    

while True:

    print(".:: UKDC ::.")
    print("1. Master Data")
    print("2. Hapus Master Data")
    pilihan = input("Pilihan 1/2: ")
    if pilihan == "1":
        function()
    elif pilihan == "2":
        fuction2()
    else:
        print("Tidak ada data untuk dihapus.")
        break
   