
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

n = int(input())
lst = [0] + list(map(int, input().split())) #각 노드의 인구수
tree = [0 for _ in range(n+1)] #노드에 연결된 길의 개수
dp = [[0,0] for _ in range(n+1)] #현재 노드가 우수마을일 경우 최대 인구수합
graph = {i:[] for i in range(1,n+1)} #노드 간 연결 상태
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    tree[a]+=1
    tree[b]+=1

result = 0
q=deque()
while(True):
    for i in range(1,n+1):
        if tree[i]==1:q.append(i) #매 반복마다 연결된 길이 1개인 노드를 큐에 더한다
    if not q: break #만약 없다면 종료
    while(q):
        now = q.popleft() #큐의 원소를 제거하고
        tree[now]-=1 #현재 노드의 길의 개수를 1줄인다
        dp[now][1]=lst[now] #현재 노드가 포함된 경우의 수에 대해 초기값으로 자기자신의 값을 더한다
        for i in graph[now]: #현재 노드와 연결된 모든 노드에 대해
            dp[now][1]+=dp[i][0] #해당 노드가 우수마을이 아닌 경우의 값을 현재 노드가 우수마을인 경우에 더하고
            dp[now][0]+=max(dp[i]) #해당 노드가 우수마을인 경우와 아닌 경우 중 값이 높은 쪽을 현재노드가 우수마을이 아닌 경우에 더한다
            tree[i]-=1 #현재 노드로 가는 길을 1감소시키고
            if tree[i]==0: tree[i]=1 #최상단 노드의 경우 값이 0이 되므로 이를 위해 값을 1로 바꾼다
        result = max(result,dp[now][0],dp[now][1]) #현재 노드의 모든 경우의 수와 기존 결과값 중 가장 큰값으로 업데이트

#print(tree)
#print(dp)
#print(graph)
print(result)


#----------------------------------------------
#문제 분야 : 다이나믹 프로그래밍
#https://www.acmicpc.net/problem/1486
