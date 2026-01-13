
n = int(input("Masukkan tinggi huruf N: "))


for i in range(n):
    for j in range(n):
       
        if j == 0 or j == n - 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()  