from math import ceil

def solution(n, stations, w):
    answer = 0
    range = w + w + 1
    
    start = 1
    for s in stations:
        answer += max(ceil((s - w - start) / range), 0)
        start = s + w + 1
        
    if n >= start:
        answer += ceil((n - start + 1) / range)
    
    return answer
