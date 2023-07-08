def solution(operations):
    answer = []
    
    for i in operations:
        num = int(i.split()[1])
        if "I" in i:
            answer.append(num)
        elif "D" in i and num == 1:
            if len(answer) != 0:
                answer.remove(max(answer))
        elif "D" in i and num == -1:
            if len(answer) != 0:
                answer.remove(min(answer))
                
    if len(answer) != 0:
        answer = [max(answer), min(answer)]
    else:
        answer = [0, 0]

    return answer
