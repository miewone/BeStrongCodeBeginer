N, M = map(int, input().split())

board = []
for _ in range(N):
    row = input()
    board.append(row)

min_count = float('inf')
 
for i in range(N - 7):
    for j in range(M - 7):
        count = 0
        
        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0: 
                    if board[i + k][j + l] != 'W':
                        count += 1
                else:  
                    if board[i + k][j + l] != 'B':
                        count += 1
        count = min(count, 64 - count)  
        min_count = min(min_count, count) 

print(min_count)
