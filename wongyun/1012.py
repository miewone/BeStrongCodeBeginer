# M 배추 밭 가로길이
# N 배추 밭 세로길이
# K 배추 개수
# https://www.acmicpc.net/problem/1012

def bfs_recu(x,y,dx,dy,graph,M,N):
    if x < 0 or x >= N or y < 0 or y >= M or graph[x][y] != 1:
        return
    graph[x][y] = 0
    for visit in range(0,4):
        bfs_recu(x+dx[visit],y+dy[visit],dx,dy,graph,M,N)

T = int(input())
for testCase in range(0,T):
    M, N, K = list(map(int, input().split(' ')))
    graph = [[0 for _ in range(0,M)] for __ in range(0,N)]
    value = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    queue = list()

    for _ in range(0,K):
        y,x = list(map(int, input().split(' ')))
        queue.append([x,y])
        graph[x][y] = 1
        
    while len(queue) != 0:
        x,y = queue.pop(0)
        if graph[x][y] == 1 : 
            value += 1
            bfs_recu(x,y,dx,dy,graph,M,N)
            
        
    print(value)
        
