size = 3
dataset = []
top = -1
status = True

def pop1():
    global top1,top2, dataset
    if top1 == -1:
        print("kosong")
    else:
        dataset[top1]= None
        top1 -=1

def pop2():
    global top1,top2, dataset
    if top2 == -1:
        print("kosong")
    else:
        dataset[top2]= None
        top2 +=1

def clear1():
    global top1,top2, dataset
    dataset.clear()
    top1 = -1
    print("Stack cleared")

def clear2():
    global top1,top2, dataset
    dataset.clear()
    top2 = +1
    print("Stack cleared")

def peek2():
    global top, dataset
    if top2 == +1:
        print("Stack is empty")
    else:
         print('Dataset: '+ str((dataset)[top]))

def peek1():
    global top1,top2, dataset
    if top1 == -1:
        print("Stack is empty")
    else:
         print('Dataset: '+ str((dataset)[top]))

def push1(data):
    global top1, top2,dataset
    if top2 - top1 > 1:
        dataset[top1 + 1] = data
        top1 += 1
    else:
        print('Stack 1 penuh..')

def push2 (data):
    global top1, top2,dataset
    if top2 - top1 > 1:
        dataset[top2 - 1] = data
        top2 -= 1
    else:
        print('Stack 2 penuh..')

    

while status==True:
    print('Dataset: '+ str(dataset))
    pilihan = int(input('Pilih: 1.Push | 2. Pop : | 3. Clear | 4. peek | 5. Exit:  '))
    if pilihan == 1:
        data = input('Input data:')
        push1()
    elif pilihan == 2:
        push2()
    elif pilihan == 3:
        pop1()
    elif pilihan == 4:
        pop2()
    
    elif pilihan == 5:
        clear1()
    
    elif pilihan == 6:
        clear2()
    elif pilihan == 7:
        peek1()
    elif pilihan == 8:
        peek2()
    elif pilihan == 9:
        break
