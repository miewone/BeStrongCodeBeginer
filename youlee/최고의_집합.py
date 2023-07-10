def solution(n, s):
    if n > s:
        return [-1]
    
    i, j = divmod(s, n)
    answer = [i] * n
    
    for _ in range(j):
        answer[_] += 1
        
    return sorted(answer)
