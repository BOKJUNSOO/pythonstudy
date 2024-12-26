# 스택
class Stack:
    def __init__(self, max_size = 8):
        self.item = [None] * max_size # 스택의 size 를 max로 지정한 경우
        self.idx = -1

    def push(self,val):
        if self.idx +1 == len(self):
            print("Stack is Full")
            return
        self.idx += 1
        self.item[self.idx] = val
        # or # list의 append 연산 # self.item.append(val) 

    def pop(self):
        if self.idx == -1: # stack is empty
            print("stack is empty")
            return None
        top_item = self.item[self.idx]
        self.item[self.idx] = None
        self.idx -= 1
        return print(top_item)
    
        # try:
        #    return self.item.pop() #defalut 값으로 pop연산
        # except IndexError:
        #    print("Stack is Empty")
    
    def top(self):
        if self.idx == -1: # stack is empty
            print("Stack is empty")
            return None
        top_item = self.item[self.idx]
        return top_item
        #try:
        #    return self.item[-1]
        #except IndexError:
        #    print("Stack is Empty")

    def __str__(self):
        return f"{self.item}"   # __str__ : return 은 문자열!

    def __len__(self):
        return len(self.item)

# 큐
class queue:
    def __init__(self):
        self.item = []
        self.first_index = 0

    def enque(self, val):
        self.item.append(val)

    def dequeue(self):
        if self.first_index == len(self.item):
            print("queue is empty")
        else:
            self.item.pop(self.first_index)
    
    def __str__(self):
        return f"{self.item}"
    

A = Stack()
A.push(3)
A.push(2)
A.push(7)
A.push(5)
A.push(88)
A.push(33)
A.push(7)
A.push(-14)
A.pop()
A.push(55)

print(A)


