k,n= map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))
start = 1
end = max(line)
 
while(start<=end):
    mid = (start+end)//2
    cnt=sum([x//mid for x in line])

    if cnt>=n:
      start=mid+1
    else:
      end=mid-1

print(end)
