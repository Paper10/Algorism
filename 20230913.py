import sys
from collections import deque
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(node * 2, start, mid)
            self.build(node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, index, value):
        diff = value - self.arr[index]
        self.arr[index] = value
        self.update_tree(1, 0, len(self.arr) - 1, index, diff)

    def update_tree(self, node, start, end, index, diff):
        if index < start or index > end:
            return

        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update_tree(node * 2, start, mid, index, diff)
            self.update_tree(node * 2 + 1, mid + 1, end, index, diff)

    def query(self, left, right):
        return self.query_tree(1, 0, len(self.arr) - 1, left, right)

    def query_tree(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self.query_tree(node * 2, start, mid, left, right)
        right_sum = self.query_tree(node * 2 + 1, mid + 1, end, left, right)
        return left_sum + right_sum

'''
# 사용 예시
arr = [1, 3, -2, 4, -1, 2, 1, -5, 4]
seg_tree = SegmentTree(arr)

print(seg_tree.query(1, 6))  # 출력: 7 (인덱스 1부터 6까지의 구간 합)

seg_tree.update(3, 8)  # 인덱스 3의 값을 8로 업데이트

print(seg_tree.query(1, 6))  # 출력: 13 (인덱스 1부터 6까지의 구간 합)
'''


N,M,K = map(int, input().split())
arr = [0]
for _ in range(N) : arr.append(int(input()))
arr_seg = SegmentTree(arr)


for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a==1:
        arr_seg.update(b, c)
    else:
        print(arr_seg.query(b, c))