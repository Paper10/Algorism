
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

class SegmentTree:

    # 세그먼트 트리 선언부
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
            self.tree[node] = min( self.tree[node * 2] , self.tree[node * 2 + 1] ) #구간 최소값

    # 세그먼트 트리 수정부
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
        else:
            self.tree[node] = self.arr[start]

    # 세그먼트 트리를 활용한 값을 구하는 부분
    def query(self, left, right):
        return self.query_tree(1, 0, len(self.arr) - 1, left, right)

    def query_tree(self, node, start, end, left, right):
        if left > end or right < start:
            return float('inf') #구간 최소값

        if left <= start and right >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_s = self.query_tree(node * 2, start, mid, left, right)
        right_s = self.query_tree(node * 2 + 1, mid + 1, end, left, right)
        return min( left_s , right_s ) #구간 최소값

n,m = map(int, input().split())

arr = []
for _ in range(n): arr.append(int(input()))
seg_tree = SegmentTree(arr)

for _ in range(m):
    a,b = map(int, input().split())
    print(seg_tree.query(a-1,b-1))


#----------------------------------------------
#문제 분야 : 세그먼트 트리
#https://www.acmicpc.net/problem/10868
