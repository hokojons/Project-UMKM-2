size = 6 
dataset = [None] * size
top1 =  -1
top2 = size 
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
    global top1, dataset
    while top1 >= 0:
        dataset[top1] = None
        top1 -= 1
    print("Stack 1 cleared")


def clear2():  
    global top2, dataset
    while top2 < size:
        dataset[top2] = None
        top2 += 1
    print("Stack 2 cleared")

def clearall():
    global top1,top2,dataset
    dataset = [None] * size
    top1 = -1
    top2 = size
    print('Stack All Clear')

def peek2():
    global top2, dataset
    if top2 == -1:
           print("Stack 2 is empty")
    else:
        print('Top of Stack 2:', dataset[top2])

def peek1():
    global top2, dataset
    if top2 == size:
        print("Stack 2 is empty")
    else:
        print('Top of Stack 1:',dataset[top1])

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
    pilihan = int(input('Pilih: 1.Push1 | 2. Push2  | 3. Pop1 | 4. pop2 | 5.Clear1 | 6.Clear2 | 7.ClearAll | 8.Peek1 | 9.Peek2 | 10.Exit : '))
    if pilihan == 1:
        data = input('Input data:')
        push1(data)
    elif pilihan == 2:
         data = input('Input data:')
         push2(data)
    elif pilihan == 3:
        pop1()
    elif pilihan == 4:
        pop2()
    
    elif pilihan == 5:
        clear1()
    
    elif pilihan == 6:
        clear2()
    elif pilihan == 7:
        clearall()

    elif pilihan == 8:
        peek1()
    elif pilihan == 9:
        peek2()
    elif pilihan == 10:
        break

