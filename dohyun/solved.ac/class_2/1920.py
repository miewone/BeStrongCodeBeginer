N = int(input())
first_data = set(map(int, input().split()))

M = int(input())
second_data = list(map(int, input().split()))

for _ in second_data:
    if _ in first_data:
        print("1")
    else:
        print("0")
