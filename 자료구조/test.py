# SinglylinkedList
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
    def push_front(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def push_back(self,key):
        v = Node(key)
        if self.size == 0:
            self.head = v
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = v
        self.size += 1
    def pop_front(self):
        if self.size == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next  # SLL 객체에 head가 멤버변수 이므로 새로 지정해줘야한다.
            self.size -= 1
            del x
        return key
    def pop_back(self):
        if self.size == 0:
            return None
        else:
            v = self.head
            prev = None
            # find tail
            while v.next is not None:
                prev = v
                v = v.next
            # set a atribute
            prev.next = None
            key = v.key
            del v
            self.size -= 1
            return key
    def search(self,key):
        v = self.head
        index = 0
        while v.next is not None:
            if v.key == key:
                return print(index)
            else:
                v = v.next
                index += 1
        return None
    def remove(self,key):
        # tail 까지 탐색
        # key 가 match 하는 node 를삭제
        # 삭제한 전 노드와 삭제한 이후 노드를 link 해줘야함
        # size를 하나 줄여아함
        v = self.head
        prev = None
        while v.next is not None:
            if v.key == key:
                self.pop_front()
                self.head = v.next
                self.size -= 1
            prev = v
            v = v.next
        return 
            

                    

            

    
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
        



L = SinglyLinkedList()
L.push_front(1)
L.push_front(2)
L.push_back(5)
L.push_front(5)
L.push_back("a")
for i in L:
    print(i)

L.search(5)
