
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

n = int(input())
lst = list(map(int, input().split()))
lst.sort() #무게 추들을 정렬 후

result = 1 #1부터 시작하여

for e in lst:
    if result<e:break #누적합이 끊어지는 순간이 잴 수 없는 무게이다
    result += e

print(result)

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/2437
