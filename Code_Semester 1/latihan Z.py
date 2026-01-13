n = int(input("maasukan nomor"))


for i in range( n ):
    for j in range( n ):
        if i ==0 or i == n-1 or j==i :

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()