
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def play(I,J):
    if board[I][J]==10: return 0 #만약 구멍이라면 0을 리턴한다
    if visit[I][J]: #만약 이미 방문한 노드라면 사이클이 이루어져 무한대로 진행가능하므로 -1 출력 후 종료한다
        print('-1')
        exit()
    if dp[I][J]>1:return dp[I][J] #만약 dp배열에 이미 값이 존재한다면 더 진행하지 않고 해당 값을 리턴한다

    for k in range(4):
        ni = I + di[k]*board[I][J]
        nj = J + dj[k]*board[I][J] #현재 노드의 수에 따라 다음 노드의 위치를 정하고
        if 0<=ni<n and 0<=nj<m: #해당 노드가 보드 내부에 있을경우
            visit[I][J]=True #현재 노드를 방문처리 후
            dp[I][J] = max(dp[I][J],play(ni,nj)+1) #재귀적으로 함수를 호출한다
            visit[I][J]=False #함수 호출 후에는 방문 처리를 해제한다
    return dp[I][J] #현재 노드의 dp값을 리턴한다

n,m = map(int, input().split())
board = []
for _ in range(n):
    ti = input()[:-1]
    tl = []
    for e in ti:
        if e=='H': tl.append(10) #구멍에 해당하는 부분을 10으로 취급하여 저장한다
        else: tl.append(int(e))
    board.append(tl)

visit = [[False]*m for _ in range(n)] #방문 여부를 저장할 배열
dp = [[1]*m for _ in range(n)] #dp값을 저장할 배열
di = [1,-1,0,0]
dj = [0,0,1,-1]
print(play(0,0)) #0,0위치에 대하여 값 출력


#----------------------------------------------
#문제 분야 : dfs
#https://www.acmicpc.net/problem/1103
