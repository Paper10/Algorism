
import heapq
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10000)

in_graph = defaultdict(list)
out_graph = defaultdict(list)

# n: 학생의 수, m: 관계의 수, x: 등수를 알고자하는 학생
n, m, x = tuple(map(int, input().split()))

for _ in range(m):  
    high, low = tuple(map(int, input().split()))

    # 자기보다 잘한 학생을 가르킨다.
    in_graph[low].append(high)
    # 자기보다 못한 학생을 가르킨다.
    out_graph[high].append(low)

def bfs(start, graph):
    visited = [False] * (n + 1)
    visited[start] = True

    q = deque([start])
    cnt = -1
    while q:
        cur = q.popleft()
        cnt += 1

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

    return cnt

# 잘한 사람을 가르키고 있는 그래프를 탐색하면서 x보다 잘한 사람들을 센다
maxRank = 1 + bfs(x, in_graph)
# 못한 사람을 가르키고 있는 그래프를 탐색하면서 x보다 못한 사람들을 센다.
minRank = n - bfs(x, out_graph)

print(maxRank, minRank)

#----------------------------------------------
#문제 분야 : DFS,BFS
#https://www.acmicpc.net/problem/17616

