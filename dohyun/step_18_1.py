class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        l = self.left.depth() if self.left else 0 # 현재 노드의 왼쪽 서브트리의 깊이를 계산
        r = self.right.depth() if self.right else 0 #현재 노드의 오른쪽 서브트리의 깊이를 계산
        return max(l, r) + 1
        # 왼쪽 서브트리와 오른쪽 서브트리 중 더 깊은 값을 선택하고 1을 더하여 현재 노드를 포함한 전체 트리의 깊이를 반환


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root:
        # 이진 트리의 루트 노드에 대해 depth() 메서드를 호출하여 전체 트리의 깊이를 계산
            return self.root.depth()
        else:
            return 0



def solution(x):
    return 0
