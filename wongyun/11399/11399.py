N = list(map(int, input().split(' ')))
P = list(map(int, input().split(' ')))
# N 사람 수
# Pi - 분 돈을 인출하는데 걸리는 시간

def min_time(P):
    P.sort()
    time = 0
    preTime = 0
    for i in range(len(P)):
        time += P[i] + preTime
        preTime += P[i]

    return time

print(min_time(P))