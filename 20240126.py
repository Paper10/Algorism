
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def go(x,y,s): 
    global h
    h = max(h,graph[y][x]) #노드를 방문할 때마다 최대값 반영

    for i in range(4): #현재 노드를 기준으로 4방향 노드에 대해
        nx = x+dx[i]
        ny = y+dy[i]
        
        if not (0<=nx<m and 0<=ny<n): continue #지도 밖의 지점이거나
        if graph[ny][nx]>graph[y][x]+t: continue
        if graph[ny][nx]+t<graph[y][x]: continue #높이의 차가 t 이상이면 중단
        
        if graph[ny][nx]>graph[y][x]: spend = s+((graph[ny][nx]-graph[y][x])*(graph[ny][nx]-graph[y][x]))
        else: spend = s+1 #노드가 높다면 차이의 제곱, 아니라면 1을 시간값에 더한다
        
        if spend+timeb[ny][nx]>d: continue #만약 해당 지점까지 왕복하는 시간이 d보다 크다면 중단
        if spend>=time[ny][nx]: continue #해당 지점까지의 기존에 저장된 시간이 현재 시간보다 작다면 중단

        time[ny][nx]=spend #현재 시간을 저장하고
        go(nx,ny,spend)#해당 노드에 대해 함수를 재귀적으로 실행

def back(x,y,s): #go 함수와 동일 구조
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if not (0<=nx<m and 0<=ny<n): continue
        if graph[ny][nx]+t<graph[y][x]: continue
        if graph[ny][nx]>graph[y][x]+t: continue
        
        if graph[ny][nx]<graph[y][x]: spend = s+((graph[y][x]-graph[ny][nx])*(graph[y][x]-graph[ny][nx]))
        else: spend = s+1 #go 함수와 반대로 노드가 낮다면 차이의 제곱, 아니라면 1을 더한다
        
        if spend>d: continue
        if spend>=timeb[ny][nx]: continue

        timeb[ny][nx]=spend
        back(nx,ny,spend)


n,m,t,d = map(int, input().split())
graph = []
for i in range(n):
    tmpi = input()[:-1]
    tmpg = []
    for e in tmpi:
        if ord('A')<=ord(e)<=ord('Z'):tmpg.append(ord(e)-ord('A'))
        elif ord('a')<=ord(e)<=ord('z'):tmpg.append(ord(e)-ord('a')+26)
    graph.append(tmpg) #알파벳에 대응하는 높이를 가지는 지도를 생성한다

dx = [1,-1,0,0]
dy = [0,0,1,-1]

time = [[INF for _ in range(m)] for _ in range(n)] #호텔에서 특정 노드까지 올라가는데 걸리는 시간
time[0][0]=0
timeb = [[INF for _ in range(m)] for _ in range(n)] #특정 지점에서 호텔까지 내려가는데 걸리는 시간
timeb[0][0]=0
h = 0
back(0,0,0) #내려가는 시간을 구한 후
go(0,0,0) #구한 내려가는 시간을 바탕으로 왕복하는 시간을 구한다

#print('-------------')
print(h)
#print('-------------')
#for e in timeb:print(e)
#print('-------------')
#for e in time:print(e)

#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/1486
