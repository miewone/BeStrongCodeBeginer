def solution(stones, k):
    answer = 0
    start, end = min(stones), max(stones)
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for s in stones:
            if (s - mid) <= 0: 
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
    return start
