
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def check(r): #방에 쓰레기가 남아있는지 검사하는 함수
    for i in range(n):
        for j in range(m):
            if r[i][j]==1:return False
    return True

def go(x,y):
    for i in range(y,n):
        for j in range(x,m): # 로봇이 아래,오른쪽 방향으로 이동하여 갈 수 있는 위치에 쓰레기가 존재한다면
            if room[i][j]==1:
                room[i][j]=0 #해당 지점의 쓰레기를 치우고
                go(j,i) #해당 지점으로 이동 후 재귀적으로 함수를 호출한다
                return 1

n,m = map(int, input().split())
room = []
for _ in range(n):room.append(list(map(int, input().split())))
result = 0
while(not check(room)): result+=go(0,0) #방에 쓰레기가 남아있는 동안 반복
print(result)


#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/1736
