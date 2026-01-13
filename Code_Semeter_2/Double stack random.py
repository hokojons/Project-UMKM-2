import random

size = 4
dataset = [None] * size
front = -1
rear = -1
status = True

front = random.randint(1, size-1)  # Fixed to avoid index out of range
rear = front

def penuh():
    return all(item is not None for item in dataset)

def kosong():
    return front == -1

def push(data):
    global dataset, front, rear
    if penuh():
        print("Stack Penuh")
    elif front == -1:
        front = rear = 0
        dataset[rear] = data
    else:
        rear = (rear + 1) % size
        dataset[rear] = data

def pop():
    global dataset, front, rear
    if kosong():
        print("Stack kosong")
        return None
    elif front == rear:
        removed_item = dataset[rear]
        dataset[rear] = None
        front = -1
        rear = -1
        return removed_item
    else:
        removed_item = dataset[rear]
        dataset[rear] = None
        if rear == 0:
            rear = size - 1
        else:
            rear -= 1
        return removed_item

def clear():
    global dataset, front, rear
    dataset = [None] * size
    front = -1
    rear = -1
    print("Stack dikosongkan")

def peek():
    print("Isi Stack saat ini:")
    for i in range(size):
        if dataset[i] is None:
            print("[ ]", end=" ")
        else:
            print(f"[{dataset[i]}]", end=" ")
    print()

def top_stack():
    if not kosong():
        print(f"Top Stack (Elemen Terakhir): {dataset[rear]}")
    else:
        print("Stack kosong, tidak ada top element")

while status:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Clear")
    print("4. Lihat Isi Stack")
    print("5. Lihat Top Stack")
    print("6. Exit")
    
    pilihan = input('Pilih menu (1-6): ')
    
    if pilihan == '1':
        data = input('Input data: ')
        push(data)
        peek()
    elif pilihan == '2':
        removed_item = pop()
        if removed_item is not None:
            print(f"Data yang dihapus: {removed_item}")
        peek()
    elif pilihan == '3':
        clear()
        peek()
    elif pilihan == '4':
        peek()
    elif pilihan == '5':
        top_stack()
    elif pilihan == '6':
        status = False
        print("Program selesai")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")