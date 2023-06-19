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


    def insertBefore(self, next, newNode):
        prev = next.prev # next node의 이전 node를 prev에 할당
        newNode.next = next # newNode의 다음 node를 next로 설정
        newNode.prev = prev # newNode의 이전 node를 prev로 설정
        prev.next = newNode # prev node의 다음 node를 newNode로 설정
        next.prev = newNode # next node의 이전 node를 newNode로 설정
        self.nodeCount += 1 # node 총 개수 증가
        return True


def solution(x):
    return 0
