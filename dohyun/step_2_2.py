def solution(L, x):
    if x not in L:
        return [-1]
        
    answer = []
    for i in range(len(L)):
        if L[i] == x:
            answer.append(i)
    return answer

