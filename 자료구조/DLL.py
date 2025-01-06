# 양방향 순환 연결 리스트
class Node:
    def __init__(self, key = None):
        self.key = key
        self.prev = self
        self.next = self
    
    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
    
    def __iter__(self):
        # self.head 는 더미노드
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return "<->".join(str(v) for v in self)
    
    def __len__(self):
        return self.size
    
    # a,b,x is node
    def splice(self,a,b,x):
        if a == None or b == None or x == None:
            return
        ap = a.prev
        bn = b.next
        xn = x.next
        # cut
        ap.next = bn
        bn.prev = ap
        
        # paste
        x.next = a
        a.prev = x

        xn.prev = b
        b.next = xn

    # 이동 및 삽입 연산
    def move_after(self,a:Node,x:Node):
        self.splice(a,a,x)
    
    def move_before(self,a:Node,x:Node):
        self.splice(a,a,x.prev)

    def push_front(self,key:int):
        self.insert_after(self.head,key)
    
    def push_back(self,key:int):
        self.insert_before(self.head,key)

    def insert_after(self,x:Node,key:int):
        self.move_after(Node(key),x)
        self.size += 1
    
    def insert_before(self,x:Node,key:int):
        self.move_before(Node(key),x)
        self.size += 1

    # 탐색연산    
    def search(self,key):
        v = self.head.next
        while v.key != None:
            if v.key == key:
                return v
            v = v.next
        return None
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    # 삭제연산

    def remove(self,v:Node):
        if v == None or v == self.head:
            return
        v.prev.next = v.next
        v.next.prev = v.prev

    def pop_front(self):
        if self.is_empty():
            return None
        key = self.head.next.key
        self.remove(self.head.next)
        return key

    def pop_back(self):
        if self.is_empty():
            return None
        key = self.head.prev.key
        self.remove(self.head.prev)
        return key

D = DoublyLinkedList()
D.push_front(1)
D.push_front(2)
D.push_front(5)
node1= D.search(5)
node2= D.search(2)
D.move_after(node1,node2)
D.insert_after(node1,8)
print(D)

