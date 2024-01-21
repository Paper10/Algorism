
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split())) 

maximum = -1 * INF
minimum = INF


def dfs(depth, total, plus, minus, multiply, divide): #dfs를 통해 현재 연산을 인자로 입력받고
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    #각 연산자에 따라 재귀적으로 함수를 호출한다
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

#----------------------------------------------
#문제 분야 : dfs
#https://www.acmicpc.net/problem/14888
