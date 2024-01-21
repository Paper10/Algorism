
import heapq
import sys
from collections import deque
input = sys.stdin.readline
H = 1000002
sys.setrecursionlimit(10000)

# n: 강의동의 수, m: 공사구간의 수, K: 건덕이가 가진 돌의 수
n, m, k = tuple(map(int, input().split()))

rocks = list(map(int, input().split()))

# 인접리스트로 그래프 구축
# graph[i][0], [1] 0 왼쪽 1 오른쪽
graph = [
    [True] * 2
    for _ in range(n + 1)
]

for _ in range(m):
    num, num2 = tuple(map(int, input().split()))

    minNum = min(num - 1, num2 - 1)
    maxNum = max(num - 1, num2 - 1)

    if minNum == 0 and maxNum == n - 1:
        graph[0][0] = False
        graph[n - 1][1] = False
    else:
        graph[minNum][1] = False
        graph[maxNum][0] = False

def bfs(start):
    q = deque([start])
    visited[start] = True
    minRock = sys.maxsize

    while q:
        cur = q.popleft()


        minRock = min(rocks[cur], minRock)

        left, right = (cur + n - 1) % n, (cur + 1) % n

        # 왼쪽으로 이동
        if graph[cur][0] == True and not visited[left]:
            q.append(left)
            visited[left] = True

        # 오른쪽으로 이동
        if graph[cur][1] == True and not visited[right]:
            q.append(right)
            visited[right] = True

    return minRock

visited = [False] * (n + 1)

bfs(0)

flag = True

# 돌다리를 두지 않아도 연결되어 있는지 확인
for i in range(0, n):
    if visited[i] == False:
        flag = False
        break

if flag:
    print("YES")
    sys.exit(0)

visited = [False] * (n + 1)

for i in range(0, n):
    # 한 연결 그래프에서 최소 돌만 연결하면 된다.
    if not visited[i]:
        ret = bfs(i)
        k -= ret
        if k < 0:
            print("NO")
            sys.exit(0)

print("YES")

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/17490
