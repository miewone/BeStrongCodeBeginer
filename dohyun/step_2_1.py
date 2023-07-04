def solution(L, x):
    answer = L
    idx = 0
    for i in range(0,len(L),1):
        if L[i] < x:
            idx +=1
    answer.insert(idx,x)
    
    return answer
