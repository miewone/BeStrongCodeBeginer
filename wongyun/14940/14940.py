from collections import deque


N, M = list(map(int,input().split(' ')))

graph = []
result_graph = [[0 for _ in range(M)] for _ in range(N)]
goalPosition = (0,0)

for i in range(N):
    input_list = list(map(int,input().split(' ')))
    for j in range(len(input_list)):
        if input_list[j] == 2:
            goalPosition = (i,j)
    graph.append(input_list)

startpoint = deque([goalPosition])

def bfs(startpoint,graph,result_graph):
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while startpoint:
        y, x = startpoint.popleft()

        for i in range(4):
            curY, curX = y+dy[i], x+dx[i]
            if curX <0 or curX >= M or curY <0 or curY >= N:
                continue
            if graph[curY][curX] == 1 :
                graph[curY][curX] = -1
                result_graph[curY][curX] = result_graph[y][x]+1
                startpoint.append((curY,curX))


bfs(startpoint,graph,result_graph)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            result_graph[i][j] = -1


for row in result_graph:
    print(' '.join(map(str,row)))


