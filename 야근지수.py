import heapq
def solution(n, works):
    answer = 0
    heap = []
    total = sum(works)
    if total <= n:
        return 0
    
    for i in works:
        heapq.heappush(heap, -i)
    
    while n > 0:
        max_hour = heapq.heappop(heap) + 1
        n -= 1
        heapq.heappush(heap, max_hour)
    
    for i in heap:
        answer += i**2

    return answer
