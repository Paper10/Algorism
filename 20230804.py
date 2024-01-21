
import heapq
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = tuple(map(int, input().split()))

board = [
    list(map(int, input().split()))
    for _ in range(n)
]

labor = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            labor.append((i, j))

ans = sys.maxsize

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

def inRange(y, x):
    return 0 <= y < n and 0 <= x < n

def virus(activated):
    global n

    temp = [
        [0] * n
        for _ in range(n)
    ]

    # 복사
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]
    # 활성화되어 있는 바이러스 표시
    for (y, x) in activated:
        temp[y][x] = 3

    q = deque([(x[0], x[1], 0, True) for x in activated])

    lastTime = 0
    # 바이러스 퍼뜨리기
    while q:
        y, x, t, isActivated = q.popleft()
        # 활성화가 되어 있지 않은 바이러스가 있는 경우에는 시간을 늘리면 안된다.
        if isActivated:
            lastTime = t

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx

            if inRange(ny, nx) and (temp[ny][nx] == 0 or temp[ny][nx] == 2):
                # 다음이 비어있는 칸이면 활성화 시켜야함
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 3
                    q.append((ny, nx, t + 1, True))
                # 비활성화되어 있는 바이러스를 활성화시키는 경우
                else:
                    temp[ny][nx] = 3
                    q.append((ny, nx, t + 1, False))

    # 바이러스가 다 퍼졌는지 확인
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 0:
                return -1

    return lastTime

for combi in list(combinations(labor, m)):
    ret = virus(combi)

    if ret != -1:
        ans = min(ret, ans)

print(-1 if ans == sys.maxsize else ans)

#----------------------------------------------
#문제 분야 : BFS
#https://www.acmicpc.net/problem/17142

