size = 5
dataset = [None] * size

def is_empty():
    return all(x is None for x in dataset)

def is_full():
    return None not in dataset

def enqueue(data):
    if is_full():
        print("Queue penuh!")
        return
    
  
    pos = 0
    while pos < size and dataset[pos] is not None:
        pos += 1
    
    
    dataset[pos] = data
    
   
    for i in range(pos, 0, -1):
        if dataset[i-1] is not None and dataset[i] < dataset[i-1]:
            dataset[i], dataset[i-1] = dataset[i-1], dataset[i]
        else:
            break

def dequeue():
    if is_empty():
        print("Queue kosong!")
        return None
    
   
    data = dataset[0]
    print("Dikeluarkan:", data)
    
   
    for i in range(size-1):
        dataset[i] = dataset[i+1]
    dataset[-1] = None
    
    return data

def clear():
    global dataset
    dataset = [None] * size

while True:
    print("\nDataset:", dataset)
    pilihan = input("Pilih: 1. Enqueue 2. Dequeue 3. Clear 4. Quit: ")
    
    if pilihan == '1':
        val = input("Masukkan data: ")
        if val.isdigit():  # Ensure numeric input
            enqueue(int(val))
        else:
            print("Masukkan angka saja!")
    elif pilihan == '2':
        dequeue()
    elif pilihan == '3':
        clear()
    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid!")