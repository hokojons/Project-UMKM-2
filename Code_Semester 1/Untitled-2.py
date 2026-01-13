for row in range(6):
    for col in range(6):
        if row==0 or row==4 or row+col==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()