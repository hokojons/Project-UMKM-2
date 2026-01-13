import random

size = 5
dataset = [None] * size
front = -1
Rear = -1
status = True

front = random.randint(1, size)
Rear = front

def push(data):
    global dataset, front, Rear
    if (Rear + 1) % size == front:
        print("Queue sudah penuh")
    elif front == -1:
        front = 0
        Rear = 0
        dataset[Rear] = data
    else:
        Rear = (Rear + 1) % size
        dataset[Rear] = data

def pop():
    global dataset, front, Rear
    if Rear == -1:
        print("Queue kosong")
        return None
    elif front == Rear:
        removed_item = dataset[Rear]
        dataset[Rear] = None
        front = -1
        Rear = -1
        return removed_item
    else:
        removed_item = dataset[Rear]
        dataset[Rear] = None
        if Rear == 0:
            Rear = size - 1
        else:
            Rear -= 1
        return removed_item

def display():
    global front, Rear
    for i in range(size):
        if dataset[i] is None:
            print("None", end=" ")
        else:
            print(dataset[i], end=" ")
    print()


while status:
    print("Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Display Queue")
    print("4. Exit")
    pilihan = input("Pilih: ")
    
    if pilihan == '1':
        data = input('Input data: ')
        push(data)
        display()
    elif pilihan == '2':
        removed_item = pop()
        if removed_item is not None:
            print(f"Deleted Rear: {removed_item}")
        display()
    elif pilihan == '3':
        display()
    elif pilihan == '4':
        status = False
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")