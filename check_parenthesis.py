def solution(s):
    stack = []
    for i in s:
        if stack == []:
            stack.append(i)
        else:
            if i == ')':
                stack.pop()
            else:
                i == '('
                stack.append(i)
    if stack == []: 
        return True
    else: 
        return False
