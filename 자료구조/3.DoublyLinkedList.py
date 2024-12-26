# 양방향 연결 리스트
class Node:
    def __init__(self, key = None):
        self.key = key
        self.prev = self
        self.next = self

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
    
    # a,b,x is node
    def splice(self, a, b, x):
        ap = a.prev
        bn = b.next
        xn = x.next
        # cut and linked
        ap.next = bn
        bn.prev = ap
        xn.next = a
        a.prev = x
        b.next = xn
        xn.prev = b
    # 삽입 연산
    def move_after(self,a,x):
        DoublyLinkedList.splice(a,a,x)
    
    def move_before(self,a,x):
        DoublyLinkedList.splice(a,a,x.prev)

    def insert_after(self,x,key):
        DoublyLinkedList.move_after(Node(key),x)
    
    def insert_before(self,x,key):
        DoublyLinkedList.move_before(Node(key),x)

    def push_front(self,key):
        DoublyLinkedList.insert_after(self.head,key)
    
    def push_back(self,key):
        DoublyLinkedList.insert_before(self.head,key)

    # 탐색연산
    def search(self,key):
        v = self.head.next
        while v != self.head:   # 조건이 false 면 탈출한다!!!!
            if v.key == key:
                return v
            v = v.next  # while 문 갱신
        return None
    
    # 삭제연산
    def remove(self,x):  # 노드 x를 삭제
        if x == None or x == self.head:
            return None
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
    def pop_front(self):
        pass
    def pop_back(self):
        pass
    
    

    def __iter__():
        pass
    def __str__(self):
        return f"{self.size}"
    def __len__(self):
        return len(self.size)