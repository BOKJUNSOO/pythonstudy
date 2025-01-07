BFS
- BFS는 너비 우선탐색이라고 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘

- ***최단경로 문제*** 를 해결할때도 이용된다.

- BFS는 큐 자료구조를 이용하며, 구체적인 동작과정은 다음과 같다.

    1) 탐색 시작 노드를 큐에 삽입하고 방문처리 한다.
    
    2) 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.

    3) 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

>> 미로최단경로(DFS는 최단경로 보장을 못 한다)

```python
# BFS Algorithm Source Code
from collections import deque
def bfs(graph,start,visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # queue가 빌 때까지 반복
    # queue가 빈다면 false 리턴
    while queue:
        # pop 으로 현재 큐에 있는 노드를 리턴
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if visited[i] == False:
                # 인접 노드를 모두 큐에 집어 넣는다
                queue.append(i)
                # 방문 처리
                visited[i] = True

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

bfs(graph, 1, visited)
```