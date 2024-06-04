
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def represent(team): #팀의 대표를 정하는 함수
    d = []
    for i in range(len(team)): d.append((i,team[i])) #graph 전체 크기가 아닌 team에 소속된 멤버의 경로만 확인하도록 매칭
    g = []
    for e in team:
        t = []
        for ee in team:
            if e==ee: t.append(0)
            elif graph[e][ee]: t.append(1)
            else: t.append(INF)
        g.append(t) #팀에 소속된 멤버만 저장하도록 재설계
    
    for k in range(len(team)):
        for i in range(len(team)):
            for j in range(len(team)):
                g[i][j]=min(g[i][j], g[i][k]+g[k][j]) #플로이드 와셜 알고리즘을 통해 최단거리 업데이트
    
    #print(d,g)
    
    result=INF
    answer=0
    for i,ti in d: #최단거리의 최대값이 가장 작은 노드를 매칭된 d배열을 참조해 반환
        if max(g[i])<result:
            result = max(g[i])
            answer = ti
    
    return answer

n = int(input())
graph = [[False for _ in range(n+1)] for _ in range(n+1)]
M = int(input())
for _ in range(M): #아는 사이를 나타내는 graph 작성
    a,b = map(int, input().split())
    graph[a][b]=True
    graph[b][a]=True

visit = [False for _ in range(n+1)]
result = 0
hresult = []
for i in range(1,n+1):
    if visit[i]: continue
    result+=1

    team = [] #bfs를 이용하여 팀 멤버 저장
    q = deque([i])
    while(q):
        now = q.popleft()
        visit[now]=True
        if not now in team: team.append(now)
        for g in range(1,n+1):
            if graph[now][g] and (not visit[g]): q.append(g)
    
    heapq.heappush(hresult, represent(team)) #해당 팀 멤버에 대해 대표선출 함수 호출

print(result)
for _ in range(result): print(heapq.heappop(hresult))    


                


#----------------------------------------------
#문제 분야 : 플로이드 와셜
#https://www.acmicpc.net/problem/2610
