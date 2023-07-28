S = input().strip()

sArr = S.split(' ')
cnt = 0 
for i in sArr:
    if len(i) > 0:
        cnt+= 1
print(cnt)