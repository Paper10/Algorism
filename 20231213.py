
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def fold(paper,d):
    w = len(paper[0]) 
    h = len(paper) #입력으로 들어온 종이의 형태의 가로,세로 길이를 저장

    #접힌 방향에 따라 반환할 배열의 크기를 설정하고 대응되는 구멍의 위치를 알려주는 배열 a 를 설정한다
    p = [[5 for _ in range(w*2)] for _ in range(h)] if d=='R' or d=='L' else [[5 for _ in range(w)] for _ in range(h*2)]
    a = [1,0,3,2] if d=='R' or d=='L' else [2,3,0,1]

    for i in range(h):
        for j in range(w): #입력으로 주어진 배열의 모든 원소를 탐색하면서

            if d=='R':
                p[i][w+j]=paper[i][j]
                p[i][w-j-1]=a[paper[i][j]]
            if d=='L':
                p[i][j]=paper[i][j]
                p[i][w*2-j-1]=a[paper[i][j]]
            if d=='U':
                p[i][j]=paper[i][j]
                p[h*2-i-1][j]=a[paper[i][j]]
            if d=='D':
                p[h+i][j]=paper[i][j]
                p[h-i-1][j]=a[paper[i][j]]
            #각 방향에 따라 알맞은 위치에 구멍을 표시한다

    return p #작업이 완료된 종이의 형태를 반환
    

N = int(input())
op = (input()).split()[::-1] #입력된 방향은 접은 방향이므로 원래 종이의 형태를 출력하기 위해 역순으로 바꿔준다
result = [[int(input())]] #초기값은 가로 1 세로 1의 입력된 구멍이 표시된 배열
for o in op: result = fold(result,o) #역순으로 만들어진 방향을 탐색하면서 fold함수를 계속 호출한다
for i in range(len(result)): # 출력
    for j in range(len(result[0])):
        print(result[i][j], end=' ')
    print('')    


#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/20187
