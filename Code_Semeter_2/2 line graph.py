po1a = [[1,2,5], [2,6,7], [1,3,6], [3,5,4], [5,6,4]]
po1aA = []
po1aB = []

start_node = po1a[0][1] 

for edge in po1a:
    if edge[0] == start_node or edge[1] == start_node:
        po1aA.append(edge)
    else:
        po1aB.append(edge)

total_bobotA = sum(edge[2] for edge in po1aA)
total_bobotB = sum(edge[2] for edge in po1aB)

print("Pola A:", po1aA)
print("Pola B:", po1aB)

if total_bobotA > total_bobotB:
    print("Bobot A lebih besar daripada B")
elif total_bobotA < total_bobotB:
    print("Bobot B lebih besar daripada A")
else:
    print("Bobot A dan B sama besar" )