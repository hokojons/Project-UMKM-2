# Initialize queue with fixed size
size = 5  # Default size
queue = [None] * size

def main():
    global size, queue
    print("Queue Operations Program")
    queue = [None] * size
    
    while True:
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if empty")
        print("4. Check if full")
        print("5. Clear queue")
        print("6. Display queue")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            item = input("Enter item to enqueue: ")
            enqueue(item)
        elif choice == '2':
            dequeue()
        elif choice == '3':
            print("Queue is empty" if is_empty() else "Queue is not empty")
        elif choice == '4':
            print("Queue is full" if is_full() else "Queue is not full")
        elif choice == '5':
            clear()
        elif choice == '6':
            display()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def enqueue(item):
    if is_full():
        print("Queue is full! Cannot enqueue", item)
    else:
        # Find first None and replace it
        for i in range(size):
            if queue[i] is None:
                queue[i] = item
                break
        print(f"Enqueued: {item}")
        display()

def dequeue():
    if is_empty():
        print("Dequeue failed - Queue is empty!")
        return None
    else:
        item = queue[0]
        for i in range(size - 1):
            queue[i] = queue[i + 1]
        queue[-1] = None
        print(f"Dequeued: {item}")
        display()
        return item

def is_empty():
    return all(item is None for item in queue)

def is_full():
    return None not in queue

def clear():
    global queue
    queue = [None] * size
    print("Queue has been cleared")
    display()

def display():
    print("Queue contents:", queue)

if __name__ == "__main__":
    main()