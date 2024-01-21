
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)


while(True):
    m,n = map(int, input().split())
    if n==0 or m==0: exit()

    graph = []
    si,sj = 0,0
    trash = 0
    for i in range(n):
        t = input()[:-1]
        for j in range(m):
            if t[j]=='o': si,sj=i,j
            if t[j]=='*': trash+=1 
        graph.append(t)

    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    visit = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((si,sj,0,0))

    while(q):
        i,j,count,move = q.popleft()
        if visit[i][j]: continue

        if graph[i][j]=='*':
            count+=1
            visit = [[False for _ in range(m)] for _ in range(n)]
            q = deque()
        
        if count==trash:
            print(move)
            q.append((0,0,0,0))
            break

        visit[i][j]=True
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<n and 0<=nj<m and graph[ni][nj]!='x':
                q.append((ni,nj,count,move+1))

    if not q: print('-1')

#----------------------------------------------
#문제 분야 : bfs
#https://www.acmicpc.net/problem/4991
