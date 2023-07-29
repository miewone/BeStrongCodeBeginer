from itertools import permutations

def check(user, ban):
    for i in range(len(user)):
        if len(user[i]) != len(ban[i]):
            return False
        for j in range(len(user[i])):
            if user[i][j] != ban[i][j] and ban[i][j] != "*":
                return False
    return True
        
def solution(user_id, banned_id):
    answer = []
    for user in permutations(user_id, len(banned_id)):
        if check(user, banned_id):
            if set(user) not in answer:
                answer.append(set(user))
    return len(answer)
