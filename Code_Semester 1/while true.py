data_list=[]
while True:
    pilihan = input("tambahkan data ke list Y/N: ")
    if pilihan == "Y":
        data = input("masukan data ")
        data_list.append(data)
    
    elif pilihan== "N":
        break

    else:
        print("pilihan tidak valid sailakan masukan Y/N")
print("\n data yang telah di masukan: ")
for i,item in enumerate(data_list,1):
    print(f"{i}. {item}")