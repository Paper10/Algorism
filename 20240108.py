
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def spring(): #봄 여름
    for i in range(n):
        for j in range(n):
            if not graph[i][j][1]: continue
            dead = 0
            graph[i][j][1].sort()
            for idx,tree in enumerate(graph[i][j][1][:]): #현재 노드의 각 나무에 대해
                if tree>graph[i][j][2]: #만약 나무가 영양성분보다 더 크다면
                    dead+=(tree//2) #해당 나무가 죽고 생성되는 영양분을 더한다
                    graph[i][j][1].remove(tree)
                else:
                    graph[i][j][2]-=tree #그렇지 않다면 영양성분을 나이만큼 제거하고
                    graph[i][j][1][idx]+=1 #나무의 나이를 1증가시킨다
            graph[i][j][2]+=dead


def fall(): #가을
    di = [-1,-1,-1,0,0,1,1,1]
    dj = [-1,0,1,-1,1,-1,0,1]
    for i in range(n):
        for j in range(n):
            for e in graph[i][j][1]: #각 노드에 대해
                if e%5==0: #나이가 5의 배수인 나무가 있으면
                    for k in range(8): #주변 노드에 나이가 1인 나무를 더한다
                        ni = i+di[k]
                        nj = j+dj[k]
                        if not(0<=ni<n and 0<=nj<n): continue
                        graph[ni][nj][1].append(1)

def winter(): #겨울
    for i in range(n):
        for j in range(n):
            graph[i][j][2]+=A[i][j] #주어진 영양만큼 각 노드에 추가한다

n,m,k = map(int, input().split())
A = []
for _ in range(n): A.append(list(map(int, input().split())))
graph = [[{1:[],2:5} for _ in range(n)] for _ in range(n)] # 1:심겨진 나무, 2:양분
for _ in range(m):
    i1,i2,i3 = map(int, input().split())
    graph[i1-1][i2-1][1].append(i3)

for _ in range(k): #각 계절을 k번 반복한다
    spring()
    fall()
    winter()
    result = 0
    for e1 in graph:
        for e2 in e1:
            #print((e2[1],e2[2]), end=' ')
            result += len(e2[1])
        #print(" ")
    #print("-------------" + str(result) + "----------------")
print(result)
    

#----------------------------------------------
#문제 분야 : 구현 
#https://www.acmicpc.net/problem/16235
