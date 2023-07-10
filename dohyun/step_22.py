class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        # 새로운 원소를 힙의 마지막에 추가
        self.data.append(item)
        # 추가된 원소의 인덱스를 저장
        index = len(self.data) - 1
        # 원소가 최대 힙의 조건을 만족하도록 상향식으로 재정렬
        while index > 1:
            parent_index = index // 2
            # 부모 노드와 추가된 원소를 비교하여 부모가 작다면 위치를 교환
            if self.data[parent_index] < self.data[index]:
                self.data[parent_index], self.data[index] = self.data[index], self.data[parent_index]
                # 인덱스를 부모 노드로 변경
                index = parent_index
            else:
                break

def solution(x):
    return 0

