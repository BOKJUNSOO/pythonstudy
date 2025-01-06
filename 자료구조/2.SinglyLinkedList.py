# 한방향 연결 리스트
class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = None
        
    def __str__(self):
        return f"{self.key}"

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return len(self.size)
    
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next

    def __str__(self):
        return "->".join(str(v) for v in self)
    
    def push_front(self,key):
        v = Node(key)
        v.next = self.head
        self.head = v
        self.size += 1

    def push_back(self,key):
        tail = Node(key)
        if self.size == 0:
            self.push_front(key= key)
        else:
            v = self.head
            # 원래 tail node를 탐색
            while v.next != None:
                v = v.next
            v.next = tail # v는 next 가 None인 node
        self.size += 1
    
    def pop_front(self):
        if self.size == 0:
            return None
        else:
            v = self.head
            key = v.key
            self.head = v.next
            self.size -= 1
            del v
        return key
    
    def pop_back(self):
        if self.size == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if self.size == 1:
                self.head = None
            else:
                prev.next = tail.next # None
            key = tail.key
            del tail
            self.size -= 1
            return key
    
    def search(self,key):
        count = 1
        v = self.head
        while v is not None:
            if v.key == key:
                print(count)
            count +=1
            v = v.next
        return
    
    def remove(self, key):
        if self.head is not None:
            if self.head.key == key:
                self.pop_front()
                return True
            v = self.head
            while v.next is not None:
                if v.next.key == key:
                    v.next = v.next.next
                    del v
                    return True
                v = v.next
        return print("key is not in list")

    def remove_all(self,key):
        pass

    def reverse(self):
        a, b = None, self.head
        while b:
            if b:
                c = b.next
                b.next = a
            a = b
            b = c
        self.head = a
            
L = SinglyLinkedList()
L.push_front("a")
L.push_front(2)
L.push_front(7)
L.push_front(8)
L.push_back(2)
print(L)
L.remove(2)
print(L)
L.reverse()
print(L)