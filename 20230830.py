from collections import deque #큐를 사용하기 위한 선언

n,k = map(int, input().split(" "))#입력부분

q = deque()
q.append([n,0])# 숫자 2개를 입력받는다
check = [True]*100001#이미 확인한 숫자를 다시 쿠에 넣지 않기 위해 방문기록을 저장하는 배열을 선언한다
while q:
    now,time = q.popleft()#큐의 데이터를 pop한 후
    if now==k:#목적지와 같다면 답을 출력한다
        print(time)
        break
    if 0<=now<=100000 and check[now]:#현재 위치가 조건에서 선언된 범위안에 들고 아직 방문하지 않았다면
        check[now]=False#방문처리하고
        if now<k:#목적지가 현재위치보다 작을경우 X+1과 X*2는 넣을필요가 없으므로 더 클때만 넣어준다
            q.append([now+1,time+1])
            q.append([now*2,time+1])
        q.append([now-1,time+1])#X-1을 삽입한다

#---------------------------------------------------------
#문제분야:BFS
#https://www.acmicpc.net/problem/1697