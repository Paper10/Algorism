
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

N = int(input())
for _ in range(N):
    n = int(input())
    result = -1
    dot = [] # 점들을 저장하는 배열
    dots = set() # in 함수의 속도를 높이기 위해 집합 사용
    for _ in range(n):
        a,b = map(int, input().split())
        dots.add((a,b))
        dot.append((a,b))
    for i in range(n):
        x1,y1 = dot[i]
        for j in range(i+1,n):
            x2,y2 = dot[j]
            dx,dy = x1-x2,y1-y2 #두 점사이의 거리를 구하고
            if result>=dx*dx+dy*dy: continue #해당 거리가 결과보다 작을경우 넘어간다
            if (x1+dy,y1-dx) in dots and (x2+dy,y2-dx) in dots: #만약 주어진 2점으로 만들 수 있는 사각형이 존재할 경우
                result = max(result, dx*dx+dy*dy) #결과를 업데이트 한다
    print(result)

#----------------------------------------------
#문제 분야 : 브루트포스
#https://www.acmicpc.net/problem/9015
