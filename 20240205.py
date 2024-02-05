
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def buy(now,price,visited):
    global result
    visited[now]=True # 현재 인원을 방문처리하고

    if False not in visited: #만약 모든 인원이 그림을 받았다면 종료
        print(n)
        exit()

    for i in range(n):
        if (not visited[i]) and graph[now][i]>=price: #만약 현재 탐색중인 사람에게 그림을 팔 수 있는 가격이면
            buy(i,graph[now][i],visited[:]) #함수를 재귀적으로 호출
    
    result = max(result, visited.count(True)) #가장 많이 방문한 노드의 개수를 저장



n = int(input())
graph = []
for _ in range(n):
    i = input()[:-1]
    t = []
    for e in i: t.append(int(e))
    graph.append(t)

result = 0
buy(0,0,[False for _ in range(n)])
print(result)

#----------------------------------------------
#문제 분야 : dfs
#https://www.acmicpc.net/problem/1029
