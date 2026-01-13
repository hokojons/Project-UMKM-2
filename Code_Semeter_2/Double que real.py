size = 5
dataset = [None] * size
head = -1
tail = size
status = True

def isFull():
    return head == tail - 1

def isEmpty():
    return head == -1 and tail == size

def enqueueLeft(data):
    global head, tail, dataset
    if isFull():
        print("Queue is full - cannot add", data)
    else:
        head += 1
        dataset[head] = data
        print(f"Added {data} to left (head: {head}, tail: {tail})")

def enqueueRight(data):
    global head, tail, dataset
    if isFull():
        print("Queue is full - cannot add", data)
    else:
        tail -= 1
        dataset[tail] = data
        print(f"Added {data} to right (head: {head}, tail: {tail})")

def dequeueLeft():
    global head, tail, dataset
    if isEmpty():
        print('Queue is empty - nothing to remove')
        return None
    removed = dataset[0]
    print(f"Removed {removed} from left")
    for i in range(1, head + 1):
        dataset[i - 1] = dataset[i]
    dataset[head] = None
    head -= 1
    return removed

def dequeueRight():
    global head, tail, dataset
    if isEmpty():
        print('Queue is empty - nothing to remove')
        return None
    removed = dataset[size - 1]
    print(f"Removed {removed} from right")
    for i in range(size - 1, tail, -1):
        dataset[i] = dataset[i - 1]
    dataset[tail] = None
    tail += 1
    return removed

def clear():
    global head, tail, dataset
    dataset = [None] * size
    head = -1
    tail = size
    print('Queue cleared')

def display():
    print("\nCurrent Queue:")
    print("Index: ", end="")
    for i in range(size):
        print(f"{i:5}", end="")
    print("\nValue: ", end="")
    for item in dataset:
        print(f"{str(item):5}", end="")
    print(f"\nStatus: Head={head}, Tail={tail}, Full={isFull()}, Empty={isEmpty()}\n")

while status:
    display()
    print("Menu:")
    print("1. Enqueue Left")
    print("2. Enqueue Right")
    print("3. Dequeue Left")
    print("4. Dequeue Right")
    print("5. Clear Queue")
    print("6. Exit")
    
    try:
        pilihan = int(input('Choose operation (1-6): '))
        if pilihan == 1:
            data = input('Enter data to add to left: ')
            enqueueLeft(data)
        elif pilihan == 2:
            data = input('Enter data to add to right: ')
            enqueueRight(data)
        elif pilihan == 3:
            dequeueLeft()
        elif pilihan == 4:
            dequeueRight()
        elif pilihan == 5:
            clear()
        elif pilihan == 6:
            print("Exiting program...")
            status = False
        else:
            print('Invalid choice - please enter 1-6')
    except ValueError:
        print("Please enter a valid number (1-6)")