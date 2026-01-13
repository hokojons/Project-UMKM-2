import random

size = 4
dataset = [None] * size
front = -1
rear = -1
status = True

front = random.randint(1, size)
rear = front
def penuh():
    return all(item is not None for item in dataset)

def push(data):
    global dataset, front, rear,status
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
    if rear == -1:
        print("Queue kosong")

    elif front == rear:
        removed_item = dataset[rear]
        dataset[rear] = None
        front = -1
        rear = -1
      
    else:
        removed_item = dataset[rear]
        dataset[rear] = None
        if rear == 0:
            rear = size - 1
        else:
            rear -= 1
        
    
def clear():
    global dataset, front, rear
    dataset = [None] * size
    front = -1


def peek():
    global front, rear
    for i in range(size):
        if dataset[i] is None:
            print("None", end=" ")
        else:
            print(dataset[i], end=" ")
    print()


while status:
    print("Menu:")
    pilihan = (input('Pilih: 1.Push | 2. Pop | 3. Clear | 4. Peek | 5. Exit : '))
    
    if pilihan == '1':
        data = input('Input data: ')
        push(data)
        peek()
    elif pilihan == '2':
        removed_item = pop()
        if removed_item is not None:
            print(f"Deleted rear: {removed_item}")
        peek()
    elif pilihan == '3':
        clear()
    elif pilihan == '4':
        peek()
    elif pilihan == '5':
        status = False
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")