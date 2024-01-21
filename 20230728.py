
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

a, b = map(str, sys.stdin.readline().split())
res = []

# 두 문자열 길이의 차이만큼 반복
for i in range(len(b) - len(a) + 1):
    cnt = 0 # 다른 문자열 개수

    # 반복문을 통해 b의 인덱스를 +i 해주면서 a의 문자열과 비교
    for j in range(len(a)):
        # 다른 문자열이면 카운트
        if a[j] != b[j + i]:
            cnt += 1

    # b의 인덱스를 +i 해주면서 비교했을 때 a의 문자열과 다른 문자열 개수를 추가
    res.append(cnt)

# 다른 문자열 개수가 제일 작을 때가 차이가 최소인 경우
print(min(res))

#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/1120

