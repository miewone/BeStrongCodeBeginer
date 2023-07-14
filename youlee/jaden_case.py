def solution(s):
    answer = []
    for i in s.split(' '):
        answer.append(i.capitalize())
    answer = " ".join(answer)
    return answer
