import heapq

import sys
N = int(sys.stdin.readline())

array = []
priority_que = []
for i in range(N):
    value = int(sys.stdin.readline())
    if value == 0 and len(array)>0:
        print(-heapq.heappop(array))
    elif value == 0 and len(array)==0:
        heapq.heappush(array,-value)
        print(-heapq.heappop(array))
    else:
        heapq.heappush(array,-value)