for i in range(5):
  for j in range(7):
      if i==0 or i==5-1 or j==0 or j==7-1:
         print("*", end=" ")
      else:
         print(" ",end=" ")   
  print()