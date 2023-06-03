T = int(input())



def fibonacci(result,n):
    if n==0: 
        result[0] += 1
        return 0
    if n==1: 
        result[1] += 1
        return 1
    else:
        return fibonacci(result,n-1)+fibonacci(result,n-2)
    
for _ in range(T):
    result = [0,0]
    fibonacci(result,int(input()))
    print(result[0], end=' ')
    print(result[1])