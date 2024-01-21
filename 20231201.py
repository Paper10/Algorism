
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m=map(int,input().split())
graph = {e:[] for e in range(1,n+1)} #각 노드로부터 연결된 노드를 기록
degree = {e:0 for e in range(1,n+1)} #각 노드로 도착하는 경로가 몇개인지 기록
for _ in range(m):
    arr = list(map(int,input().split()))[1:]
    for i in range(len(arr)-1):
        a,b = arr[i],arr[i+1]
        graph[a].append(b)
        degree[b]+=1 #두 딕셔너리에 값 저장
print(graph,degree)

result = []
q=deque([e for e in degree if degree[e]==0]) #노드로 들어오는 경로가 없는 노드들을 초기값으로 넣는다
while(q):
    now = q.popleft() 
    result.append(now) #큐에 가장 먼저 들어온 노드를 방문한 후
    for e in graph[now]: #해당 노드로부터 출발하는 경로의 도착 노드들에 대해
        degree[e]-=1 # 도착노드의 경로 수를 1 줄이고
        if degree[e]==0: #그 값이 0일경우
            q.append(e) #큐에 추가한다

for e in range(1,n+1):
    if not degree[e]==0 : #큐에 원소가 없는데 아직 경로가 남아있는 노드가 존재한다면 순환이 발생하여 가능한 답이 없다는 의미
        print(0) #0 출력후 종료
        exit()
for e in result: print(e) #값 출력


#----------------------------------------------
#문제 분야 : 위상 정렬
#https://www.acmicpc.net/problem/2623
