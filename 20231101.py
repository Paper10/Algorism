
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

n,m = map(int, input().split())
problem = [[] for _ in range(n+1)] #특정 문제 다음에 풀어야 하는 문제를 저장하는 배열
line = [0]*(n+1) #특정 문제보다 먼저 풀어야 하는 문제의 개수를 저장하는 배열
for _ in range(m):
    a,b = map(int, input().split())
    line[b]+=1
    problem[a].append(b)

#print(problem)
#print(line)

heap = [] # 가능한한 오름차순으로 정렬하기 위해 우선순위 큐를 사용한다
for i in range(1,n+1):
    if line[i]==0: heapq.heappush(heap, i) #먼저 풀어야하는 문제가 없는 문제들을 초기값으로 넣어준다
while(heap): #큐에 문제가 존재할 동안
    t = heapq.heappop(heap) #큐에서 pop한 후 출력한 뒤
    print(t, end=' ')
    for e in problem[t]: #해당 문제 다음에 풀어야 하는 문제들에 대해
        line[e]-=1 # line배열의 해당 문제의 개수를 1줄이고
        if line[e]==0: heapq.heappush(heap, e) #만약 더이상 먼저 푸는 문제가 없어진 경우 우선순위 큐에 삽입한다



#----------------------------------------------
#문제 분야 : 우선순위 큐
#https://www.acmicpc.net/problem/1766
