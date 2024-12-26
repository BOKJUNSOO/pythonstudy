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

    def push_front(self,key):
        new_node = Node(key)    # 객체 생성
        new_node.next = self.head   # 생성된 객체의 next는 none 인데(defalut), SLL의 head로 지정
        self.head = new_node        # SSL의 head
        self.size += 1              

    def __len__(self):
        return len(self.size)
    
    def push_back(self,key):    # tail을 찾고 tail의 next를 tail로 지정
        v = Node(key)
        if self.size == 0:      # len(self) --> 객체 사이즈를 측정(__len__?)
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next    
            tail.next = v
        self.size += 1
    
    def pop_front(self):    # head 노드를 삭제하고 값을 리턴
        if self.size == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
        return key

    def pop_back(self):     # tail 노드를 삭제하고 값을 리턴
        if self.size == 0:
            return None
        else:
        # running tech
            prev = None
            tail = self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if self.size == 1:
                self.head = None
            else:
                prev.next = tail.next
                key = tail.key
                del tail
                self.size -= 1
                return key
            
    def remove2(self,key):
        v = self.head
        prev = None
        while v is not None:
            if v.key == key:
                self.pop_front()
                return True
            prev = self.head
            v = v.next
        return False

    def remove(self,key):
        if self.head is not None:
            if self.head.key == key:
                self.pop_front()
                return True
            v = self.head
            while v.next is not None:
                if v.next.key == key:
                    v.next = v.next.next
                    return True
                v = v.next
        return print("key is not in list")
                    

    def search(self, key):
        # key 값의 node 를 return 없으면 none return
        count = 1
        v = self.head
        while v is not None:
            if v.key == key:
                print(count)
            count += 1
            v = v.next
        return None
    
    def __iter__(self):     # 연결리스트 객체를 iterable 하게 사용가능한 메쏘드 구현
        v = self.head
        while v != None:
            yield v
            v = v.next
    # for i in L:
    #   print(i)
            
    def __str__(self):
        return f"{self.size}"
    

L = SinglyLinkedList()
L.push_front("a")
L.push_front(2)
L.push_front(7)
L.push_front(8)
L.push_front(3)

L.remove2(8)
for i in L:
    print(i)





