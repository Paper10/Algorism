
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)


n,k,m = map(int, input().split())
node = [[] for _ in range(n+1)] #각 노드에 연결된 튜브의 인덱스를 저장하는 배열
tube = [] #튜브에 연결된 노드를 저장하는 배열
for i in range(m): 
    t = list(map(int, input().split()))
    tube.append(t)
    for e in t:
        node[e].append(i)

visitN = [False for _ in range(n+1)] #각 노드에 방문했는지 여부를 저장
visitT = [False for _ in range(m)] #각 튜브에 방문했는지 여부를 저장
q = deque()
q.append((1,1)) #초기값을 넣고
while(q):
    now,count = q.popleft()
    if now==n: #만약 마지막 노드라면 count 출력
        print(count)
        exit()
    visitN[now]=True #현재 노드를 방문처리하고
    for tu in node[now]:
        if not visitT[tu]: #현재 노드에 연결된 튜브 중 아직 방문하지 않은 튜브에 대해
            visitT[tu] = True #해당 튜브를 방문처리하고
            for no in tube[tu]:
                if not visitN[no]: q.append((no,count+1)) #해당 튜브에 연결된 노드 중 아직 방문하지 않은 노드를 큐에 삽입한다
    

print('-1') #만약 마지막 노드에 도달할 수 없으면 -1 출력
#----------------------------------------------
#문제 분야 : bfs
#https://www.acmicpc.net/problem/5214
