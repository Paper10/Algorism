
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def bfs(X,Y):
    q = deque([(X,Y)]) #큐를 선언하고 큐가 빌때까지 반복한다
    while(q):
        x,y = q.popleft()
        visit[x][y]=True

        #현재 노드에서 불을 킬 수 있는 스위치의 노드에 대해
        #스위치를 켠 후 결과에 1을 더하고
        #만약 불을 킨 노드와 인접한 노드중 이미 방문한 노드가 존재한다면 해당 노드또한 방문이 가능한 노드라는 의미이므로
        #큐에 해당 노드를 넣어준다
        if (x,y) in dic:
            for i,j in dic[(x,y)]: 
                if not graph[i][j]:
                    graph[i][j] = True
                    result[0]+=1
                    for k in range(4):
                        ni = i+dx[k]
                        nj = j+dy[k]
                        if not (0<=ni<n and 0<=nj<n): continue
                        if visit[ni][nj]: q.append((i,j))

        #현재 노드의 각 방향에 대해
        #불이 켜져있지만 아직 방문하지 않은 노드가 있다면 큐에 넣어준다
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not (0<=nx<n and 0<=ny<n): continue
            if (not visit[nx][ny]) and graph[nx][ny]: q.append((nx,ny))


#값을 입력받고 불켜짐 여부를 저장하는 grpah와 방문 여부를 저장하는 visit 배열을 선언한다
n,m = map(int, input().split())
graph = [[False for _ in range(n)] for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
graph[0][0]=True #초기값은 방문처리

#각 노드에서 스위치가 있는 노드를 표시하는 리스트를 만든다
dic = {}
for _ in range(m):
    ax,ay,bx,by = map(int, input().split())
    if (ax-1,ay-1) in dic : dic[(ax-1,ay-1)].append((bx-1,by-1))
    else: dic[(ax-1,ay-1)] = [(bx-1,by-1)]
#print(dic)

#0,0 에서 bfs함수를 호출한다
result = [1]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
bfs(0,0)
print(result[0])


#----------------------------------------------
#문제 분야 : bfs
#https://www.acmicpc.net/problem/11967
