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
