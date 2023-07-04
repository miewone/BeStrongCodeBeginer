
import sys


def check(num, broken_buttons):
    num = str(num)
    for i in num:
        if i in broken_buttons:
            return False
    return True

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken_buttons = list(map(str, sys.stdin.readline().split()))

min_click = abs(N - 100) 

for i in range(1_000_001): 
    if check(i, broken_buttons):
        min_click = min(min_click, len(str(i)) + abs(i - N)) 

print(min_click)

def solution(N,M,brokenButtons):
    if N == "100":
        return 0
    nowWatchChannel = 100
    numberBrokenButtons = [ int(i) for i in brokenButtons]
    nNumber = int(N)
    cnt = 0
    canMaxChannel = ""
    for i in N:
        cnt += 1
        if i in brokenButtons:
            canButton = int(i)
            while canButton in numberBrokenButtons:
                canButton -= 1
            canMaxChannel += str(canButton)
        else:
            canMaxChannel += i
    
    gap = int(N) - int(canMaxChannel)
    return gap + cnt
    
    
    
    
    
    
    

N = input()
M = int(input())
brokenButtons = None
if M:
    brokenButtons = list(input().split(' '))

print(solution(N,M,brokenButtons))
    

