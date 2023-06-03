# M : 가로 길이
# N : 세로 길이
# H : 높이 길이
from collections import deque

M, N, H = list(map(int,input().split(' ')))
def bfs(graph,startPoints:deque,h,n,m):
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    dz = [-1,1]

    while startPoints:
        H, Y, X = startPoints.popleft()
        for i in range(4):
            curY, curX = dy[i] + Y, dx[i] + X
            if curX <0 or curY<0 or curY>=n  or curX >= m or graph[H][curY][curX] != 0:
                continue
            
            graph[H][curY][curX] = graph[H][Y][X] +1
            cnt = graph[H][curY][curX]
            startPoints.append((H,curY,curX))
            
        
        for hfor in range(2):
            curZ = dz[hfor] + H
            if curZ<0 or curZ>=h or graph[curZ][Y][X] != 0:
                continue
            
            graph[curZ][Y][X] = graph[H][Y][X] +1
            
            startPoints.append((curZ,Y,X))
    
graph = []

for _ in range(H):
    graphfloor = []
    for _ in range(N):
        graphfloor.append(list(map(int,input().split(' '))))
    graph.append(graphfloor)

startPoints = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                startPoints.append((h,n,m))
result = bfs(graph,startPoints,H,N,M)

is_all_done = all(graph[h][i][j] != 0 for i in range(N) for j in range(M) for h in range(H))
if not is_all_done:
    print("-1")
else:
    max_day = max([max(map(max, floor)) for floor in graph]) - 1  # 각 층에서 가장 큰 값을 찾아 최대값 계산
    print(max_day)




# 0 0 0 0 0
# 0 0 0 0 0 level 2
# 0 0 0 0 0
# =========
# 0 0 0 0 0
# 0 0 1 0 0 level 1
# 0 0 0 0 0