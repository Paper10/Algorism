from collections import deque

#행렬의 크기 N,M과 지도를 표현하는 2차원 배열을 입력받는다
n,m = map(int, input().split())
map = []
for _ in range(n):
    arr = [int(char) for char in list(input())]
    map.append(arr)

#지도 데이터를 원활하게 사용하기 위한 배열 선언
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q=deque()#큐를 선언하고
q.append([0,0])#첫 위치인 0,0 을 큐에 초기값으로 넣어준다

while q:#큐에 원소가 있는 동안
    x,y = q.popleft()#큐의 데이터를 pop하여
    if x==m-1 and y==n-1:#목적지에 도착했다면
        print(map[y][x])#거리를 출력하고 종료
        break
    for i in range(4):#현재 노드의 4방향에 대해 각각 판단
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and map[ny][nx]==1:#만약 대상 노드가 지도 내부에 있고 아직 방문하지 않은 길이라면
            map[ny][nx]=map[y][x]+1
            q.append([nx,ny])#거리를 기록하고 해당 노드를 큐에 넣는다
#-------------------------------------------
#문제 분야 : BFS
#https://www.acmicpc.net/problem/2178