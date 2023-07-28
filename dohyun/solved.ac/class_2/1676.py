n = int(input())

count = 0
while n > 1:
    count += n // 5
    n = n // 5

print(count)
