import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visit = [-1] * (n + 1) #방문 여부를 판단하는 배열을 생성하고
    que = deque() #큐를 생성후 인자로 받은 시작노드를 초기값으로 넣는다
    que.append(start)
    visit[start] = 0
    Max = [0, 0]

    while que: #큐에 원소가 존재하는 동안
        num = que.popleft() #원소를 pop하여
        for node, dis in graph[num]: #간선 정보에서 해당 노드로부터 시작되는 모든 간선에 대해
            if visit[node] == -1:#도착 노드에 아직 방문하지 않았으면
                visit[node] = visit[num] + dis #현재 노드까지의 거리와 도착 노드 사이의 거리를 더해 저장한다
                que.append(node)
                if Max[0] < visit[node]: #만약 도착 노드까지의 거리가 지금까지의 거리 중 가장 멀다면
                    Max = [visit[node], node] #Max에 해당 노드와 노드까지의 거리를 저장한다
    return Max

#노드의 개수와 간선을 입력받기 위한 배열을 생성한다
n = int(input())
graph = [[] for _ in range(n + 1)]

#각 간선의 정보를 (node,distance) 형태로 저장한다
for _ in range(n):
    a = list(map(int, input().split()))
    for e in range(1, len(a)-1, 2):
        graph[a[0]].append((a[e], a[e + 1]))

dis, node = bfs(1)#임의의 노드로부터 거리 중 가장 먼 노드를 찾는다
dis, node = bfs(node)#해당 노드로부터 가장 긴 거리를 찾는다
print(dis)#거리를 출력한다
#--------------------------------------------------------
#문제 분야 : BFS,DFS
#https://www.acmicpc.net/problem/1167