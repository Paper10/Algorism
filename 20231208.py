
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
_max = max(tree) # 가져갈 수 있는 나무의 높이의 최댓값
_min = 1 # 가져갈 수 있는 나무의 높이의 최솟값

# 이분탐색
# 최댓값이 최솟값보다 작아질때까지 반복
while _max >= _min:
    mid = (_max + _min) // 2 # 절단기의 높이
    res = 0 # 가져갈 수 있는 나무의 높이의 합

    # 반복문을 통해 절단기로 나무를 자른 후
    # 가져갈 수 있는 나무의 높이를 더한다.
    for i in tree:
        if i > mid:
            res += i - mid

            # 가져갈 수 있는 나무의 높이가
            # 가져가려하는 나무의 높이보다 크면 반복을 멈춘다.
            if res > m:
                break

    # 가져갈 수 있는 나무의 높이가 가져가려야 하는 높이보다 크거나 같으면 절단기의 높이를 올려주기 위해
    # 가져갈 수 있는 나무의 높이의 최솟값을 절단기의 높이에 + 1 해준 값으로 초기화한다.
    if res >= m:
        _min = mid + 1

    # 가져갈 수 있는 나무의 높이가 가져가려야 하는 높이보다 작으면 절단기의 높이를 내려주기 위해
    # 가져갈 수 있는 나무의 높이의 최댓댓값을 절단기의 이에 - 1 해준 값으로 초기화한다.
    else:
        _max = mid - 1

# 절단기의 최댓값 출력
print(_max)

#----------------------------------------------
#문제 분야 : 이진탐색
#https://www.acmicpc.net/problem/2805

