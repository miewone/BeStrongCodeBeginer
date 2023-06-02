# T : 테이스 케이스
# N : 건물의 개수
# K : 건물간의 건설순서 규칙의 총 개수

# D[배열] : 각 건물당 건설에 걸리는 시간
# X, Y : 건설 순서
# W : 승리하기 위해 건설해야 할 건물의 번호
from collections import deque
import sys
minTime = 0
T = int(sys.stdin.readline())

for TEST_CASE in range(0,T):
    N, K = list(map(int, sys.stdin.readline().split(' ')))
    dp = [-99] *(N+1)

    graph = [[] for _ in range(N+1)]
    inDegree = [0] * (N+1)
    weight = [0] * (N+1)
    values = [0] * (N+1)
    for idx,item in enumerate(list(map(int, sys.stdin.readline().split(' ')))):
        values[idx+1] = item
    
    for _ in range(K):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        graph[a].append(b)
        inDegree[b] += 1
    W = int(sys.stdin.readline())
    
    # W에서 부터 뒤로 돌아감.
    
    
    q = deque([node for node in range(1, N+1) if not inDegree[node]])
    
    
    for i in q:
        dp[i] = values[i]
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            dp[i] = max(dp[i],dp[cur]+values[i])
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)
        

    print(dp[W])
 