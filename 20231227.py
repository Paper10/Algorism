
import heapq
import sys
from collections import deque
input = sys.stdin.readline
MAP = map(int,input().split())
sys.setrecursionlimit(10000)

#입력
n,m = MAP
graph = []
for _ in range(n): graph.append(input()[:-1])
visit = [] #해당 위치를 방문했는지 알려주는 같은크기의 배열 선언
for _ in range(n): visit.append([0 for _ in range(m)])
d = {'D':(1,0),'U':(-1,0),'R':(0,1),'L':(0,-1)} #방향 딕셔너리 선언

cycle = 1
result = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j]==0: continue #만약 방문한 노드라면 넘어간다
        
        di,dj = i,j #현재노드를 기준으로
        while(True):
            visit[di][dj]=cycle
            di,dj = di + d[graph[di][dj]][0], dj + d[graph[di][dj]][1] #현재 노드의 방향을 기반으로 다음 방문 노드를 정하고

            if visit[di][dj]==0: continue
            else:
                if visit[di][dj]==cycle: result+=1 #만약 다음 노드가 현재 사이클과 같은 값이라면 사이클이 발생하므로 이 사이클 중 1곳에 안전지대를 놓아야 한다
                cycle+=1 #만약 아니라면 기존 사이클에 들어가는 노드이므로 추가로 안전지대를 놓을 필요가 없다
                break

print(result)

#----------------------------------------------
#문제 분야 : DFS
#https://www.acmicpc.net/problem/16724
