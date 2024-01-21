import sys
from collections import deque
input = sys.stdin.readline

#입력부
n,m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)] # 특정 위치에서의 목적지까지 갈수있는 경우의 수를 저장하는 배열과
d = [(1,0),(-1,0),(0,1),(0,-1)] # 스택 구현시 편의를 위해 방향벡터 배열을 선언

def dfs(x,y):
    global visit
    #만약 목적지에 도달했을경우 1을 반환
    if x==m-1 and y==n-1:
        return 1
    #만약 목적지를 가던 도중 이미 방문한 위치를 만났다면 해당 위치에서 목적지까지 가는 경우의 수를 참조 후 반환
    elif visit[y][x]>0:
        return visit[y][x]
    else:
        for i in range(4):
            nx,ny = x+d[i][0],y+d[i][1] #현재 위치 기준 4방향에 대해
            if 0<=nx<m and 0<=ny<n and mat[ny][nx]<mat[y][x]: #해당 위치가 지도안에 들어와있고 다음 위치의 높이가 더 낮다면
                visit[y][x] += dfs(nx,ny) #다음 위치를 기준으로 dfs를 재귀적으로 호출한다
    return visit[y][x] #위 과정이 전부 끝나면 visit 배열에 각 칸에서 목적지까지의 경우의 수가 저장되므로 이를 반환한다

print(dfs(0,0))
#------------------------------------------------------------------
#문제 분야 : DFS
#https://www.acmicpc.net/problem/1520