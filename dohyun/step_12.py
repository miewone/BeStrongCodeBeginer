class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for token in S:
        if token.isalpha():  # 변수인 경우
            answer += token
        elif token == '(':  # 여는 괄호인 경우
            opStack.push(token)
        elif token == ')':  # 닫는 괄호인 경우
            while not opStack.isEmpty() and opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()  # 여는 괄호 제거
        else:  # 연산자인 경우
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                answer += opStack.pop()
            opStack.push(token)
    
    while not opStack.isEmpty():  # 스택에 남아 있는 연산자들을 모두 pop
        answer += opStack.pop()
    
    return answer
