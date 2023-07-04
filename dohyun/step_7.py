class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):  # 리스트를 순회하는 메서드
        result = []  # 결과를 저장할 빈 리스트 생성
        curr = self.head  # 현재 노드를 head로 초기화
        while curr is not None:  # 리스트의 끝까지
            result.append(curr.data)  # 현재 노드의 데이터를 결과 리스트에 추가
            curr = curr.next  # curr을 다음 노드로 이동
        return result  # 결과 리스트 반환

# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0
