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
    
