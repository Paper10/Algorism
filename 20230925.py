import heapq
import sys
from collections import deque
input = sys.stdin.readline

#입력부분
N = int(input())
matrix = [list(map(str, input().strip())) for _ in range(N)]

row = 0
column = 0

#가로로 누울때
for y in range(N):
    cnt = 0
    for x in range(N): # 각 줄을 탐색하면서
        if matrix[y][x] == '.':
            cnt += 1 #만약 빈칸이라면 cnt를 늘리고
        elif matrix[y][x] == 'X':
            if cnt >= 2:
                row += 1 #cnt가 2인 상태에서 짐을 만난다면 결과에 1을 더하고
            cnt = 0 #cnt를 0으로 초기화한다
    if cnt >= 2:
        row += 1 #끝에 도달했을떄고 마찬가지 과정을 진행한다
    cnt = 0

# 세로로 누울때
# 가로로 누울때와 같다
for x in range(N):
    cnt = 0
    for y in range(N):
        if matrix[y][x] == '.':
            cnt += 1
        elif matrix[y][x] == 'X':
            if cnt >= 2:
                column += 1
            cnt = 0
    if cnt >= 2:
        column += 1
    cnt = 0

print(row, column)

#---------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/1652