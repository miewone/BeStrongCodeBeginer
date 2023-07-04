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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
            continue
        if token == ")":
            while not opStack.isEmpty():
                item =opStack.pop()
                if item == "(":
                    break
                postfixList.append(item)
        elif token in "*+/-(":
            if opStack.isEmpty():
                opStack.push(token)
            elif token == "(":
                opStack.push(token)
            else:
                while prec[token] <= prec[opStack.peek()]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
                opStack.push(token)
        else :
            postfixList.append(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    answer = 0  # 계산 결과를 저장할 변수
    numStack = ArrayStack()  # 숫자(피연산자)를 저장할 스택
    for token in tokenList:
        if type(token) is int:  # 피연산자인 경우
            numStack.push(token)
        else:  # 연산자인 경우
            af = numStack.pop()  # 스택에서 두 번째 피연산자
            bf = numStack.pop()  # 스택에서 첫 번째 피연산자
            if token == "+":
                answer = bf + af
            elif token == "-":
                answer = bf - af 
            elif token == "*":
                answer = bf * af
            elif token == "/":
                answer = bf / af
            numStack.push(answer)  # 연산 결과를 스택에 저장

    return numStack.pop()  # 최종 결과를 스택에서 꺼내 반환

def evaluate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

    
def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
