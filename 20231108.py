
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

n,m = map(int, input().split())
sa,sb = 0,0
ea,eb = 0,0
graph = []
for i in range(n): #지도를 입력받으며 시작지점과 끝지점을 저장한다
    tmp = input()[:-1]
    for j in range(m):
        if tmp[j]=='F': ea,eb = i,j
        if tmp[j]=='S': sa,sb = i,j
    graph.append(tmp)

di = [1,-1,0,0]
dj = [0,0,1,-1]

visit = [[[INF,INF] for _ in range(m)] for _ in range(n)] #특정 위치까지 도달할 경우 지나치는 쓰레기와 쓰레기 옆의 개수를 저장
q=deque()
q.append((sa,sb,0,0)) #시작위치를 초기값으로 넣어준다
while(q):
    i,j,t,s = q.popleft()
    if visit[i][j][0]>t: visit[i][j]=[t,s]
    elif visit[i][j][0]==t and visit[i][j][1]>s: visit[i][j]=[t,s] #현재 위치의 쓰레기 및 쓰레기 옆 개수가 업데이트 된다면 업데이트 후 진행
    else: continue #아니라면 진행하지 않는다

    nt,ns = t,s
    if graph[i][j]=='S': #만약 시작지점이라면 쓰레기 업데이트 없이 인접 위치를 모두 큐에 삽입한다
        for k in range(4):
            if 0<=i+di[k]<n and 0<=j+dj[k]<m: q.append((i+di[k],j+dj[k],0,0))
        continue
    elif graph[i][j]=='g': nt+=1 #쓰레기가 있는 위치라면 쓰레기 개수를 1 더한다
    else:
        for k in range(4): #쓰레기와 인접한 위치라면 쓰레기 옆 개수를 1 더한다
            if 0<=i+di[k]<n and 0<=j+dj[k]<m and graph[i+di[k]][j+dj[k]]=='g':
                ns+=1
                break
    
    for k in range(4): #업데이트한 쓰레기 개수를 반영한 다음 인접 노드를 큐에 삽입한다
        if 0<=i+di[k]<n and 0<=j+dj[k]<m: q.append((i+di[k],j+dj[k],nt,ns))

#for e in visit:print(e)
print(visit[ea][eb][0],visit[ea][eb][1])

#----------------------------------------------
#문제 분야 : bfs
#https://www.acmicpc.net/problem/1445
