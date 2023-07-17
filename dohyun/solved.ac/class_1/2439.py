line = int(input())

for i in range(1, line+1):
    blank = " " * (line-i)
    star = "*" * i
    print(blank + star)