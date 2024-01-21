
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

nums = list(map(int, input().split()))

# (두 눈덩이의 합, 선택된 눈덩이 i, j)
snowmans = [
    (nums[i] + nums[j] , i,  j)
    for i in range(n)
    for j in range(i + 1, n)
    if i != j
]

# 두 눈덩이의 합을 오름차순으로 정렬
snowmans.sort()

left, right = 0, 1
ans = sys.maxsize

while right < len(snowmans):
    sm1, i1, j1 = snowmans[left]
    sm2, i2, j2 = snowmans[right]

    left += 1
    right += 1

    # 눈덩이의 조합이 겹치는 경우가 있으면 넘어간다.
    if i1 == i2 or i1 == j2:
        continue
    if j1 == i2 or j1 == j2:
        continue

    ans = min(ans, sm2 - sm1)

print(ans)

#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/20366

