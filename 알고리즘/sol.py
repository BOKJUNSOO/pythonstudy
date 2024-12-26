# 그래프1(연습) DOTS
n,m = map(int,input().split())
data = [[]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    data[_] = list(map(str, input().strip()))

# 시작점 정보는 가지고 있어야 하므로 함수스택안에 저장
def dfs(x,y,letter,count,start_x,start_y):
    global flag
    # 4방향에 대해서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 벗어나면 continue
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        #해당 각주처리된 코드는 있으면 안됨
        #if visit[nx][ny] == 1:
        #    continue

        # 아직 방문을 하지 않았고, 탐색중인 점이라면
        if visit[nx][ny] == 0 and data[nx][ny] == letter:
            # 방문 처리
            visit[nx][ny] = 1
            # 다음 노드 count + 1
            dfs(nx,ny,letter,count+1,start_x,start_y)
        # 더 이상 방문할 곳이 없다면 (재귀 종료하면서)
        elif count >= 4 and start_x == nx and start_y == ny:
                # print(count) 연결된 고리에 포함된 점의 갯수
                flag = True
                return
    return
                
flag = False

for i in range(n):
    for j in range(m):
        start_x = i
        start_y = j
        # 방문리스트를 사용해야 하나? 직접 data에 방문처리하고 다른 letter을 사용할때
        # 다시 data를 불러와도 되는 것 아닌가?
        # 바이러스 연구소 문제와 차이점
        visit = [[0]*m for _ in range(n)]
        visit[start_x][start_y] = 1
        dfs(i,j,data[i][j],1,start_x,start_y)
        if flag:
            print('Yes')
            exit()
        else:
            continue

if not flag:
    print('No')

# 미로 최단거리 + 아파트 갯수새기 문제 방문기록 + 함수스택내부의 count 써보기
