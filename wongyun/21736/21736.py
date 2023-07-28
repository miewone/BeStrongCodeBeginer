from collections import deque


N,M = list(map(int,input().split(' ')))


graph = []
start = (0, 0)

for i in range(N):
    row = list(input())
    for j in range(len(row)):
        if row[j] == "I":
            start = (i,j)
        
    graph.append(row)
    
num_P = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            start = (i, j)
        elif graph[i][j] == 'P':
            num_P += 1

def bfs(start, graph):
    visited = [[False]*M for _ in range(N)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    count_P = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and graph[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny))
                if graph[nx][ny] == 'P':
                    count_P += 1
    return count_P

cnt = bfs(start, graph)
print(cnt if cnt != 0 else 'TT')
