import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def findloop(now,way): #루프를 찾는 함수
    global loop
    global visit
    if visit[now]==True: #만약 방문처리된 노드를 만났다면 루프가 발생한것이므로
        if not loop: loop = way[way.index(now):] #저장된 지금까지의 경로에서 루프 부분을 저장
        return
    visit[now]=True #현재 노드를 방문처리하고
    for i in range(1,n+1):
        if graph[now][i]==True and not i==way[-1]: #연결된 노드중 직전에 방문한 노드를 제외한 노드에 대해
            findloop(i,way+[now]) #경로에 현재 노드를 저장하고 다음 노드을 인수로 재귀적 호출


n = int(input())
graph = [[False for _ in range(n+1)] for _ in range(n+1)] #간선들의 정보
visit = [False for _ in range(n+1)]#루프를 찾는 과정에서 해당 노드의 방문 여부 저장
loop = [] #루프를 저장
for _ in range(n):
    a,b = map(int,input().split())
    graph[a][b]=True
    graph[b][a]=True #간선들의 정보를 입력받아 저장

findloop(1,[0]) #루프를 찾는 함수

result = [0 if i in loop else -1 for i in range(n+1)] #루프까지의 거리를 저장하는 배열, 루프 부분은 0으로 처리
for e in loop: #루프의 모든 노드에 대해 해당 노드로부터 시작하는 노드를 탐색한다
    q = deque([(e,0)]) #현재 값을 초기 값으로 설정
    while q:
        now,dis = q.popleft()
        result[now]=dis #현재 노드의 거리를 저장하고 
        for i in range(1,n+1):#현재 노드에 연결된 다른 노드들에 대해
            if graph[now][i]==True and (result[i]==-1 or result[i]>dis+1): #아직 방문하지 않은 노드거나 현재 거리가 더 짧은 노드일 경우
                q.append((i,dis+1)) #큐에 해당 노드를 삽입한다

for e in result[1:]: print(e, end=' ') #결과 출력
#----------------------------------------------
#문제 분야 : dfs,bfs
#https://www.acmicpc.net/problem/16947
