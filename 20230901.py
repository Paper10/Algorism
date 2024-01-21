from collections import deque

#토마토 박스의 형태를 입력
n,m = map(int, input().split(" "))
box = []
for _ in range(m):
    arr = list(map(int, input().split()))
    box.append(arr)

#큐 자료구조를 편하게 다루기 위해 방향 배열 선언
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()#큐 선언
for i in range(m):
    for j in range(n):
        if box[i][j]==1:
            q.append([i,j]) #전체 박스를 탐색하면서 익은 토마토의 위치를 큐의 초기값으로 넣어준다

while q: #더이상 큐 내부에 탐색할 노드가 없을때까지 반복
    y,x = q.popleft()#큐의 자료를 pop하여
    for i in range(4):#각 방향의 노드를 탐색한다
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and box[ny][nx]==0:#만약 해당 노드가 박스를 벗어나지 않았고 아직 익지 않은 토마토이면
            box[ny][nx]=box[y][x]+1#현재노드의 값에 +1을 하여 익을때까지 걸린 시간을 표시하고
            q.append([ny,nx])#큐에 해당 노드를 더한다

not_finished = False #박스내부의 토마토가 완전히 익었는지 판단하는 변수
result = 0 #결과값
for i in range(m):
    for j in range(n):#박스를 전부 탐색하며
        if box[i][j]==0:
            not_finished = True#만약 아직 익지않은 토마토가 남아있을 경우 not_finished변수를 True로 바꿔준다
        else:
            result = max(result, box[i][j])#각 노드를 탐색하며 더 큰값을 저장한다

#not_finished 변수가 True가 되었다면 -1을, 그렇지 않다면 result값을 출력한다 (익은 토마토를 나타내는 수가 1이었으므로 result-1값 출력)
print(-1 if not_finished else result-1)

#-----------------------------------------------------------
#문제 분야 : BFS
#https://www.acmicpc.net/problem/7576