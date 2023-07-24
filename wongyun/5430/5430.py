import sys
import re
from collections import deque

T = int(sys.stdin.readline().strip('\n'))

for _ in range(T):
    p = sys.stdin.readline().strip('\n')
    n = int(sys.stdin.readline().strip('\n'))
    array = sys.stdin.readline().strip('\n')[1:-1]
    if array == "":
        arr = deque()
    else:
        arr = deque(map(int, array.split(',')))

    reverse = False
    error = False
    for command in p:
        if command == 'R':
            reverse = not reverse
        elif command == 'D':
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                error = True
                break
    if not error:
        if reverse:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')