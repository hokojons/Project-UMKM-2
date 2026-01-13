size =5 
dataset = [None] * size

def is_empty():
    return all(x is None for x in dataset)

def is_full():
    return None not in dataset

def enqueue(data):
    if is_full():
        print("Queue is full")
        return
    
    # Find first empty slot
    pos = 0
    while pos < size and dataset[pos] is not None:
        pos += 1
    
    # Insert the new data
    dataset[pos] = data
    
    # Bubble up to maintain order
    for i in range(pos, 0, -1):
        if dataset[i-1] is not None and dataset[i] < dataset[i-1]:  # Fix: Check "is not None"
            dataset[i], dataset[i-1] = dataset[i-1], dataset[i]
        else:
            break

def dequeue():
    if is_empty():
        print("Queue is empty")
        return None
    

    data=dataset[0]
    print("Dikeluarkan", data)

    for i in range(size-1):
        dataset[i] = dataset[i+1]
    dataset[-1] = None

    return data

while True:
    print("\nDataset:", dataset)
    pilihan = input("Pilih: 1. Enqueue 2. Dequeue 3. Quit: ")
    
    if pilihan == '1':
        val = input("Masukkan data: ")
        if val.isdigit(): 
            enqueue(int(val))
        else:
            print("Masukkan angka saja!")
    elif pilihan == '2':
        dequeue()
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid!")