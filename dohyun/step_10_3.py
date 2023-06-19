class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next # prev 뒤에 있는 node를 curr로 설정
        if curr == self.tail:  # 삭제할 node가 없는 경우
            return None
        next = curr.next # next는 curr 다음 node로 설정
        prev.next = next # prev의 next를 next로 변경
        next.prev = prev # next의 prev를 prev로 변경
        self.nodeCount -= 1 # 전체 노드 개수를 하나 감소
        return curr.data

    def popBefore(self, next):
        curr = next.prev
        if curr == self.head:  
            return None
        prev = curr.prev
        next.prev = prev
        prev.next = next
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos <0 or pos > self.nodeCount: # pos가 0보다 작거나 현재 연결 리스트의 노드 개수보다 크면 error 반환
            raise IndexError
        else: # 그렇지 않으면 삭제하려는 node의 이전 node를 찾아 prev 변수에 저장
            prev = self.getAt(pos - 1)
            return self.popAfter(prev)




def solution(x):
    return 0
