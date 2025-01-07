`탐색`
- 탐색 이란 많은 양의 데이터 중에서 "원하는 데이터"를 찾는 과정을 말합니다.

- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다.

- DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형!!

`DFS`
- DFS 는 깊이 우선 탐색 이라고도 부르며 , 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

- DFS는 스택 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다.
    1) 탐색 시작 노드(1)를 스택에 삽입하고 방문처리를 합니다.

    2) 시작노드를 출력하고 시작노드와 인접한 노드를 모두 스택에 추가합니다.

    3) 스택의 최상단 노드를 꺼내고 출력합니다.

    4) 스택의 최상단 노드에 인접한 노드가 존재한다면 인접한 노드를 다시 스택에 추가합니다.
    
    (반복)
    >> 얼음틀

```python
#참고) 그래프 구현\
line, node = map(int, input().split())
node = node +1 # dummy node

#
graph = [[] for _ in range(node)]

# 간선 정보 입력
for i in range(line):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

# 각 노드 오름차순 (문제조건)
for i in range(1,node):
    graph[i].sort()


# DFS Algorithm Source Code
def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end =' ')
    # 해당노드의 인접 노드에 대해서
    for i in graph[v]:
        # 인접노드가 아직 방문하지 않았다면 (노드리스트에 솔팅된 순서에 따라)
        if visited[i] == False:
            # 재귀함수를 계속 호출하여 더 깊은곳 까지 탐색하는 알고리즘!!
            dfs(graph,i,visited)


# 그래프 표현 2차원 리스트
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 호출
dfs(graph , 1, visited)
```