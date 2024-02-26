
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)] #도시를 저장하는 배열

chicken = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 2]
house = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 1]
minimum = INF

for case in combinations(chicken, M):
    total = 0
    for i in range(len(house)):
        mid_sum = 1e9
        for c in case:
            mid_sum = min(mid_sum, abs(house[i][0] - c[0]) + abs(house[i][1] - c[1]))
        total += mid_sum
    if total < minimum:
        minimum = total

print(minimum)


#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/15686
