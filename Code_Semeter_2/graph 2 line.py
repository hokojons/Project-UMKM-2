po1a = [[1,2,5], [2,6,7], [1,3,6], [3,5,4], [5,6,4]]
polaA = []
po1aB = []
temp = po1a[0][1]
i = 0
bobota = 0
bobotB = 0

polaA.append(po1a[0])

for x, y, z in po1a:
    if i == 0:
        i += 1
        continue 
    if x == temp:
        polaA.append(po1a[i])
        temp = y
    else:
        po1aB.append(po1a[i])
    i += 1

print("pola A:", polaA)
print("pola B:", po1aB)