"""
def solution(L, x):
    idx = 0
    while idx < len(L) and L[idx] != x:
        idx += 1
    if idx < len(L):
        return idx  
    else:
        return -1 
"""
def solution(L, x):
    left, right = 0, len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1  

