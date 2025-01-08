import heapq

# Max heap
class heap:
    def __init__(self, A=[]):
        self.A = A
        self.make_heap()
    
    def __str__(self):
        return str(self.A)
    
    def make_heap(self):
        n = len(self.A)
        for k in range(n-1,-1,-1):
            self.heapify_down(k,n)
    # A[k]를 힙성질이 만족하는 위치로 내려가면서 재배치
    def heapify_down(self,k,n):
        # 리프노드가 아니라면 while문 실행
        # n 은 전체 노드의 갯수수
        while 2*k+1 < n:
            L, R = 2*k+1 , 2*k+2
            # 부분트리중 가장 큰 값의 인덱스를 m에 저장장
            if self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R<n and self.A[R] > self.A[m]:
                m = R
            # 확인하는 노드가 최댓값이 아니라면
            if m !=k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break
    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1 ,-1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n -1
            self.heapify_down(0,n) # A[0] 부터 정렬
        
    # 올라가면서 A[k]를 재 배치
    def heapify_up(self,k):
        # 루트노드에 아직 도달하지 않고, 부모노드의 값이 더 작다면
        while k>0 and self.A[(k-1)//2] < self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            # while 문 조건 갱신
            k = (k-1)//2

    def insert(self,key):
        self.A.append(key)
        # A에 추가된 가장 마지막 원소에 대해서 heap 구조 만들기
        self.heapify_up(len(self.A)-1)
    
    # 루트노드의 값을 삭제하는 함수
    def delete_max(self):
        if len(self.A) == 0: return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        # 가장 왼쪽에 위치하는 루트노드를 pop
        self.A.pop(0)
        self.heapify_down(0, len(self.A))
        return key

a = [2,8,6,1,10,15,3,12,11,21]
heap_ = heap(a)
print("make heap:",heap_.A)
heap_.heap_sort()
print("heap sorting :",heap_.A)
heap_.delete_max()
print("delete max:",heap_.A)


#mod = heapq
#mod._heapify_max(a)
#for _ in a:
#    print(_)
