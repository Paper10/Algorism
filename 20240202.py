
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def move(y,x,s,D): #상어의 좌표,속력,방향을 입력받고 상어가 이동할 좌표로 움직인다
    d = D-1
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    for _ in range(s):
        if y==0 and d==0: d=1
        if y==r-1 and d==1: d=0 
        if x==c-1 and d==2: d=3 
        if x==0 and d==3: d=2 #만약 경계선에 도달할 경우 방향을 바꾼다
        x+=dx[d]
        y+=dy[d]
    return y,x,d+1


r,c,m = map(int, input().split())
sea = [[0 for _ in range(c)] for _ in range(r)] #바다의 상태를 저장하는 배열
shark = [[0]] # 상어의 정보를 저장한느 배열
for i in range(1,m+1):
    t = list(map(int,input().split()))
    t[0]-=1
    t[1]-=1
    shark.append(t)
    sea[t[0]][t[1]]=i

result = 0
for i in range(c):

    for j in range(r): #먼저 어부가 있는 열의 모든 상어를 잡는다
        if not sea[j][i]==0:
            result+=shark[sea[j][i]][4]
            shark[sea[j][i]]=[0]
            sea[j][i]=0
            break

    sea = [[0 for _ in range(c)] for _ in range(r)] #바다의 상태를 초기화하고

    for j in range(1,m+1):
        s = shark[j]
        if len(s)==1:continue
        n0,n1,nd = move(s[0],s[1],s[2],s[3]) #현재 탐색중인 상어의 위치를 파악한 뒤
        if sea[n0][n1]==0:
            sea[n0][n1]=j
            s[0]=n0
            s[1]=n1
            s[3]=nd #빈공간이면 해당 위치로 상어의 상태를 업데이트하고
        else:
            if s[4]>shark[sea[n0][n1]][4]:sea[n0][n1]=j #만약 이미 상어가 존재한다면 더 크기가 큰 상어를 배치한다
            else: shark[j]=[0]

print(result)
#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/17143
