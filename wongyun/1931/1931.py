N = int(input())

conferenceList = []
for _ in range(N):
    start, end = map(int, input().split())
    conferenceList.append((start, end))


conferenceList.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0
for conf in conferenceList:
    if conf[0] >= end_time:  
        end_time = conf[1]   
        cnt += 1

print(cnt)
