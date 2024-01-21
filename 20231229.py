
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(i,j):
    if visit[i][j]: return visit[i][j] #만약 이미 방문한 노드라면 그대로 반환

    visit[i][j]=1 #해당 노드를 방문처리하고
    for k in range(4):
        di,dj = i+dir[k][0], j+dir[k][1] #각 방향의 노드에 대해
        if di<0 or di>=n or dj<0 or dj>=n : continue #범위를 벗어나거나
        if graph[di][dj]<=graph[i][j] : continue #더 작은 값을 가지는 노드는 넘어간다
        visit[i][j] = max(dfs(di,dj)+1,visit[i][j]) #해당 노드로부터 dfs를 재귀적으로 호출하여 최댓값으로 업데이트
        
    
    return visit[i][j] #업데이트된 값을 반환

#입력
n = int(input())
graph = []
for _ in range(n): graph.append(list(map(int,input().split())))
visit = [] #해당 노드에서 출발하여 도달할수 있는 최대 노드개수를 저장
for _ in range(n): visit.append([0 for _ in range(n)])
dir = [(1,0),(-1,0),(0,1),(0,-1)]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j)) #각 노드에 대해 dfs를 실행하여 최댓값으로 업데이트

print(result)

#----------------------------------------------4
#문제 분야 : 다이나믹 프로그래밍 + dfs
#https://www.acmicpc.net/problem/1937
