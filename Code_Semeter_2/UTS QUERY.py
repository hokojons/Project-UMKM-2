class SortedQueue:
    def __init__(self, size=5):
        self.queue = [None] * size
        self.size = size
    
    def enqueue(self, value):
        if None not in self.queue:
            print("Queue is full")
            return
        
        # Find the first empty slot and insert
        for i in range(self.size):
            if self.queue[i] is None:
                self.queue[i] = value
                break
        
        # Sort the queue, moving None values to the end
        temp = [x for x in self.queue if x is not None]
        temp.sort()
        temp.extend([None] * (self.size - len(temp)))
        self.queue = temp
    
    def dequeue(self):
        if all(x is None for x in self.queue):
            print("Queue is empty")
            return None
        
        # Find the first non-None value
        for i in range(self.size):
            if self.queue[i] is not None:
                value = self.queue[i]
                # Shift all elements left
                for j in range(i, self.size - 1):
                    self.queue[j] = self.queue[j + 1]
                self.queue[-1] = None
                return value
        return None
    
    def display(self):
        print(f"Dataset: {self.queue}")

def main():
    queue = SortedQueue()
    
    while True:
        queue.display()
        choice = input("Pilih: 1.Enqueue | 2.Dequeue : ")
        
        if choice == '1':
            data = input("Input data: ")
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        else:
            print("Pilihan tidak valid")
            continue

if __name__ == "__main__":
    main()