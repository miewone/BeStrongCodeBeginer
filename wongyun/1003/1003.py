T = int(input())

dp = [[0]*2 for _ in range(41)] 
# dp[i][0]은 i번째 피보나치 수에서 0이 호출되는 횟수, dp[i][1]은 1이 호출되는 횟수
dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1


for _ in range(T):
    N = int(input())
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print(dp[N][0], dp[N][1])
