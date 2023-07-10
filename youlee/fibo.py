def solution(n):
    answer = []
    for i in range(n+1): 
        if i < 2:
            answer.append(i)
        else:
            result = (answer[i-1] + answer[i-2]) % 1234567
            answer.append(result)
    return answer[-1]
