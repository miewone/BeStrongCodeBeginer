from collections import deque

def bfs(n,m,v,graph):
    visited = [0] * (n+1)
    q = deque([v])
    visited[v] = 1
    while q:
        cur = q.popleft()
        
        for i in graph[cur]:
            if visited[i] !=1:
                q.append(i)
                visited[i] = 1
                
        print(cur, end=' ')
    
        
    
def dfs(n,m,v,graph):
    visited = [0] * (n+1)

    dfs_visit(v,graph,visited)

def dfs_visit(v,graph,visited):
    if visited[v] == 1: return    
    visited[v] = 1
    print(v, end=' ')
    
    for i in graph[v]:
        dfs_visit(i,graph,visited)
    
# N : 정점의 개수
# M : 간선의 개수
# Vs

N, M, V = list(map(int,input().split(' ')))


graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int,input().split(' ')))
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i] = sorted(graph[i])

dfs(N,0,V,graph)
print('')
bfs(N,0,V,graph)
    