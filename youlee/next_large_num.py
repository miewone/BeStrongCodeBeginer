def solution(n):
    answer = n+1
    cnt = format(n, 'b').count('1')
    
    while True:
        ans_cnt = format(answer, 'b').count('1')
        if cnt == ans_cnt:
            break
        answer += 1
        
    return answer
