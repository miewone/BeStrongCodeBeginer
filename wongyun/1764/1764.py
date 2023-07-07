N, M = list(map(int,input().split(' ')))


noListen = list()
noSaw = list()
seeThat = list()
for i in range(N):
    noListen.append(input())

for i in range(M):
    noSaw.append(input())

for i in noListen:
    if i in noSaw:
        seeThat.append(i)
        
seeThat.sort()
for i in seeThat:
    print(i)


