class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        if prev.next is None: # prev가 마지막일때 None 반환
            return None
        curr = prev.next # 삭제할 node를 curr에 할당
        if self.tail == curr: # 삭제할 node가 list에 마지막일 경우
            self.tail = prev # 마지막을 prev(삭제할 node의 이전 node)로 변경
            prev.next = None # prev의 다음을 삭제할 node 다음으로 설정
        else: # 삭제할 node가 마지막이 아닐 경우
            prev.next = curr.next # prev의 다음 node를 삭제할 node로 설정
            
        self.nodeCount -= 1 # node를 하나 삭제했으므로 총 개수 -1
        return curr.data # 삭제한 node의 데이터 반환


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount: # 삭제할 node의 위치의 범위 지정
            raise IndexError # Index error 발생
        prev = self.getAT(pos - 1) # 삭제할 node의 이전 node를 찾아 prev에 할당
        return self.popAfter(prev) # prev node 다음의 node 삭제

def solution(x):
    return 0
