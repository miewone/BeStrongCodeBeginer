# N : 정점의 개수
# M : 간선의 개수
import sys
sys.setrecursionlimit(10000)
def dfs(graph,point,visitedList):
    if visitedList[point] != 0:
        return
    visitedList[point] = 1
    for i in graph[point]:
        if visitedList[point] != 0:
            dfs(graph,i,visitedList)

N, M = list(map(int,sys.stdin.readline().split(' ')))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int,sys.stdin.readline().split(' ')))
    graph[a].append(b)
    graph[b].append(a)
    
visitedCnt = 0
visitedList = [0] * (N+1)

for i in range(1,N+1):
    if visitedList[i] == 0:
        dfs(graph,i,visitedList)
        visitedCnt += 1
print(visitedCnt)
