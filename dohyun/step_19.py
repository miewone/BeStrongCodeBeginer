class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        result = []  # 방문한 노드를 저장할 리스트
        if self.root is None:
            return result

        queue = ArrayQueue()  # 큐 생성
        queue.enqueue(self.root)  # 루트 노드를 큐에 삽입

        while not queue.isEmpty():
            node = queue.dequeue()  # 큐에서 노드를 하나 꺼냄
            result.append(node.data)  # 방문한 노드를 결과 리스트에 추가

            # 왼쪽 자식 노드가 있다면 큐에 삽입
            if node.left is not None:
                queue.enqueue(node.left)

            # 오른쪽 자식 노드가 있다면 큐에 삽입
            if node.right is not None:
                queue.enqueue(node.right)

        return result


def solution(x):
    return 0
