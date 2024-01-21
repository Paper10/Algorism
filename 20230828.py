from collections import deque

#행렬의 크기 N,M과 지도를 표현하는 2차원 배열을 입력받는다
n,m = map(int, input().split(" "))
map = []
for i in range(n):
    arr = [int(char) for char in list(input())]
    map.append(arr)

#지도 데이터를 원활하게 사용하기 위한 배열 선언
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#BFS 알고리즘 실행을 위한 큐 자료구조 선언 및 지도의 특정 위치의 방문기록을 저장하기 위한 3차원 배열 선언
#방문기록 visited는 벽을 깨지않고 방문한 기록과 벽을 꺠고 방문한 기록을 저장하기 위해
#[0,0]으로 이루어진 지도와 같은 크기의 배열
#인덱스 0은 벽을 깨지않고, 1은 벽을 깨고 방문한 기록
result = -1
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
q = deque()

q.append([0,0,1,0]) #큐의 첫 데이터는 0,0 좌표이며 거리값은 1이고 벽을 부수지않았으므로 punch값에 0저장
while(q):
    x,y,distance,punch = q.popleft()
    visit[y][x][punch]=1 #punch값에 따라 알맞은 인덱스에 방문을 기록한다
    if x==m-1 and y==n-1: #만약 목표지점에 도달했다면 result에 distance값을 저장하고 루프를 빠져나온다
        result = distance #BFS알고리즘 특성상 가장 먼저 목표지점에 방문했을떄의 distance가 최단거리이다
        break
    for i in range(4): #현재노드 기준 동서남북 4방향을 각각 검증한다
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n: #다음 노드가 map안에 들어와야 한다 
            if visit[ny][nx][punch]==0 and map[ny][nx]==0: #다음 노드를 방문한적이 없으면서 벽이 아닌경우
                q.append([nx,ny,distance+1,punch])
            elif punch==0 and visit[ny][nx][0]==0 and map[ny][nx]==1: #벽을 부수지 않았고 다음 노드가 벽이면서 아직 방문하지 않았을경우
                q.append([nx,ny,distance+1,1])
print(result) #결과를 출력한다

#---------------------------------------------------------------------------------
#문제 분야 : BFS
#https://www.acmicpc.net/problem/2206