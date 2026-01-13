import random

size = 6
dataset = [None] * size
head = -1
tail = -1

def is_empty():
    return head == -1

def is_full():
    return (tail + 1) % size == head

def enqueue(data):
    global head, tail
    if is_full():
        print("Queue penuh!")
        return

    if is_empty():
        head = tail = 0  # Start both head and tail at the first index
    else:
        tail = (tail + 1) % size

    dataset[tail] = data

def dequeue():
    global head, tail
    if is_empty():
        print("Queue kosong!")
        return

    print("Dikeluarkan:", dataset[head])
    if head == tail:  # Queue becomes empty after this dequeue
        head = tail = -1
    else:
        head = (head + 1) % size

def clear():
    global dataset, head, tail
    dataset = [None] * size
    head = tail = -1

while True:
    print("\nDataset:", dataset)
    pilihan = int(input("Pilih: 1. Enqueue 2. Dequeue 3. Clear 4. Quit: "))
    
    if pilihan == 1:
        val = input("Masukkan data: ")
        enqueue(val)
    elif pilihan == 2:
        dequeue()
    elif pilihan == 3:
        clear()
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak valid!")
