numbers_list = [1,3,5,6,8,9,10,24,35,36,38,40,44,46,48,50,66,77,88,89,90,91,92,93,95,97,99,100,355,565,878,900]

def search_number(number_list, search_value):
    if search_value in number_list:
        index = number_list.index(search_value)
        return f"{search_value} Nomor dalam list pada indeks {index}"
    else:
        return f"{search_value} Nomor tidak dalam list"

while True:
    elemen_cari = int(input("Masukkan angka yang ingin dicari (0 untuk berhenti): "))
    if elemen_cari == 0:
        print("Program berhenti.")
        break
    print(search_number(numbers_list, elemen_cari))