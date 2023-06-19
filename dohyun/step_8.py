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


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        # 인자로 받은 위치 값이 연결 리스트 범위 내에 있는지 확인
        # 범위를 벗어나면 IndexError를 발생
        if pos < 1 or pos > self.nodeCount:
            raise IndexError('Index out of range')

        # 연결 리스트에 노드가 하나만 있는 경우
        if self.nodeCount == 1:
            node = self.head  # 제거할 노드를 참조
            self.head = None  # 연결 리스트의 head를 None으로 설정
            self.tail = None  # 연결 리스트의 tail를 None으로 설정
        else:
            # 제거할 노드가 첫 번째 노드인 경우, head를 업데이트
            if pos == 1:
                node = self.head  # 제거할 노드를 참조
                self.head = node.next  # head를 제거할 노드의 다음 노드로 업데이트
            else:
                prev = self.getAt(pos - 1)  # 제거할 노드의 바로 이전 노드를 참조
                node = prev.next  # 제거할 노드를 참조
                prev.next = node.next  # 이전 노드의 next를 제거할 노드의 다음 노드로 연결

                # 제거할 노드가 마지막 노드인 경우, tail을 업데이트
                if pos == self.nodeCount:
                    self.tail = prev

        # 노드 개수를 감소
        self.nodeCount -= 1
        # 제거된 노드의 데이터를 반환
        return node.data  



    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0
