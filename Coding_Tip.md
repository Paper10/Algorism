# 코딩 팁

코딩문제를 풀면서 배운 내용들을 끄적이는 공간


## 우선순위 큐 (힙) 사용법

힙 선언은 일반적인 배열과 동일하다

힙은 배열의 원소를 자동으로 오름차순 정렬한다

힙의 원소들에 -1을 곱하여 내림차순 힙처럼 동작할 수 있다

```
import heapq
heap = [] 
```

힙에 원소를 삽입하는 방법

```
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print(heap) # [1,3,5]
```

힙의 원소를 빼내는 방법

```
P0 = heapq.heappop(heap)
print(P0) # P0 == 1
```

## 세그먼트 트리

배열의 구간합, 구간의 최소값, 구간의 최댓값을 더 빠르게 구할 수 있다

```
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
            # self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1] #구간합
            # self.tree[node] = max( self.tree[node * 2] , self.tree[node * 2 + 1] ) #구간 최대값
            # self.tree[node] = min( self.tree[node * 2] , self.tree[node * 2 + 1] ) #구간 최소값

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
        # 구간 최대값, 구간 최소값 코드일 경우 아래 else 구문 추가
        else:
            self.tree[node] = self.arr[start]

    # 세그먼트 트리를 활용한 값을 구하는 부분
    def query(self, left, right):
        return self.query_tree(1, 0, len(self.arr) - 1, left, right)

    def query_tree(self, node, start, end, left, right):
        if left > end or right < start:
            # return 0 #구간합
            # return float('-inf') #구간 최대값
            # return float('inf') #구간 최소값

        if left <= start and right >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_s = self.query_tree(node * 2, start, mid, left, right)
        right_s = self.query_tree(node * 2 + 1, mid + 1, end, left, right)
        # return left_s + right_s #구간합
        # return max( left_s , right_s ) #구간 최대값
        # return min( left_s , right_s ) #구간 최소값


# 사용 예시
arr = [1, 3, -2, 4, -1, 2, 1, -5, 4]
seg_tree = SegmentTree(arr)

print(seg_tree.query(1, 6))  # 출력: 7 (인덱스 1부터 6까지의 구간 합/구간 최소값/구간 최대값)

seg_tree.update(3, 8)  # 인덱스 3의 값을 8로 업데이트

print(seg_tree.query(1, 6))  # 출력: 13 (인덱스 1부터 6까지의 구간 합/구간 최소값/구간 최대값)

```
## 플로이드 와셜 알고리즘

각 노드가 특정 값을 가진 간선으로 연결된 그래프에 대해

특정 노드에서 다른 노드까지의 가능한 길 중 최솟값을 저장하는 알고리즘

```
def floyd():
    for k in range(1,len(graph)+1):
        for i in range(1,len(graph)+1):
            for j in range(1,len(graph)+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

```