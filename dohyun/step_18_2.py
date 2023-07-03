class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):
        # 전위 순회 결과를 저장할 리스트를 생성
        traversal = []
        # 현재 노드의 데이터를 결과 리스트에 추가
        traversal.append(self.data)
        # 왼쪽 서브트리를 전위 순회하고 결과를 리스트에 추가
        if self.left:
            traversal += self.left.preorder()
        # 오른쪽 서브트리를 전위 순회하고 결과를 리스트에 추가
        if self.right:
            traversal += self.right.preorder()
        # 전위 순회 결과 리스트를 반환
        return traversal

class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []


def solution(x):
    return 0
