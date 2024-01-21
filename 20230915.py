import heapq
import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(graph, start):
    #모든 거리정보를 무한으로 설정 후 시작 노드의 거리를 0으로 초기화한다
    distances = {e: float('inf') for e in range(1,n+1)}
    distances[start] = 0

    #우선순위 큐에 시작노드에 대한 (거리,노드) 정보를 넣는다.
    priority_queue = [(0, start)]

    while priority_queue:
        dis, node = heapq.heappop(priority_queue) #우선순위 큐에서 거리가 제일 작은 노드를 pop한다

        if dis > distances[node]: # 만약 pop한 거리가 현재 저장된 거리보다 더 큰값이라면 무시한다
            continue

        for i in range(1,n+1):
            if graph[node][i]==0 : continue
            distance = dis + graph[node][i] # pop한 노드와 인접한 노드들 까지의 거리를 계산한다.
            if distance < distances[i]: # 계산한 노드까지의 거리가 저장된 노드까지의 거리보다 작을경우 
                distances[i] = distance # 계산한 거리로 갱신하고
                heapq.heappush(priority_queue, (distance, i)) # 해당 노드를 우선순위 큐에 삽입한다
                # 이 과정으로 가장 작은 거리값이 나올떄 까지 계속해서 거리를 갱신할 수 있다.

    return distances

# 노드 및 간선정보 입력
n,m,x = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

#해당 간선 정보를 이용하여 함수를 실행한다
away = dijkstra(graph, x)

#반대 방향에서의 최단거리를 구하기 위해 간선정보를 뒤집어준다
for i in range(n+1):
    for j in range(i,n+1):
        graph[i][j], graph[j][i] = graph[j][i], graph[i][j]

#뒤집은 함수를 기반으로 함수를 실행한다
come = dijkstra(graph, x)

#반환된 두 딕셔너리에서 같은 노드에 대한 값의 합 중 가장 큰 값을 출력한다
print(max([come[i]+away[i] for i in range(1,n+1)]))