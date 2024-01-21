
import heapq
import sys
import copy
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def count_ways(coins, total):
    dp = [0] * (total + 1)
    dp[0] = 1 #가격+1 만큼의 길이를 가지는 배열을 선언후에 인덱스 0에 해당하는 값을 1로 설정한다

    for coin in coins: #각 코인 종류를 탐색하면서
        for i in range(coin, total + 1):
            dp[i] += dp[i - coin] #현재 탐색중인 가격의 종류의 수에 현재 코인 종류만큼 뺀 위치의 값을 더한다

    return dp[total] #마지막 값을 출력

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

result = count_ways(coins, k)
print(result)


#----------------------------------------------
#문제 분야 : 다이나믹 프로그래밍
#https://www.acmicpc.net/problem/2293
