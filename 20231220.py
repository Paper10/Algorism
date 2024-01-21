
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

carrots = []

n, t = tuple(map(int, input().split()))

for _ in range(n):
    w, p = tuple(map(int, input().split()))
    carrots.append((p, w))

# p가 높은순으로 내림차순 정렬
carrots.sort(reverse=True)

ans = 0
for p, w in carrots:
    if t == 0:
        break
    ans += p * (t - 1) + w
    t -= 1

print(ans)

#----------------------------------------------
#문제 분야 : 정렬
#https://www.acmicpc.net/problem/18234

