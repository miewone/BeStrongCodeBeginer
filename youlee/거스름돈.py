def solution(n, money):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin]
    
    answer = dp[n] % 1000000007
    
    return answer
