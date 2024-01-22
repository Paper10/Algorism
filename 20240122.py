
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(1000000)

def find(r,c):
    global count
    if r<0 or r>=n or c<0 or c>=m: return True #만약 경계바깥이라면 true
    if way[r][c]: return True #올바른 길로 인정된 노드라면 true
    if visit[r][c]: return False #만약 이미 방문한 노드라면 false
    visit[r][c]=True #현재 노드를 방문처리하고
    if graph[r][c]=='D': dr,dc = r+1,c
    elif graph[r][c]=='U': dr,dc = r-1,c
    elif graph[r][c]=='R': dr,dc = r,c+1
    elif graph[r][c]=='L': dr,dc = r,c-1 #다음 노드를 지정
    if find(dr,dc): #만약 다음 노드가 true값을 반환한다면
        count+=1 #결과를 1 증가시키고
        way[r][c]=True #현재노드를 올바른 길로 저장한 후
        return True #true반환
    else: return False #아니라면 false 반환


n,m = map(int, input().split())
count = 0 #결과를 저장할 변수
visit = [[False for _ in range(m)] for _ in range(n)] #노드가 이미 방문한 노드인지 저장
way = [[False for _ in range(m)] for _ in range(n)] #노드가 올바른 길인지 저장
graph = []
for _ in range(n):graph.append(input())
for i in range(n):
    for j in range(m):
        if not visit[i][j]: find(i,j) #방문하지 않은 노드에 대해 함수 실행
print(count)


        

#----------------------------------------------
#문제 분야 : dfs
#https://www.acmicpc.net/problem/17090
