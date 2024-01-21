
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

M = 1000000
t,a,s,b = map(int, input().split())
count = [0 for _ in range(t+1)] #각 숫자의 개수를 저장하는 배열
dp = [[0 for _ in range(b+1)] for _ in range(t+1)] #특정 숫자까지 고려했을때 가능한 배열의 개수를 저장하는 배열
d = list(map(int, input().split()))
for e in d: count[e]+=1
for i in range(count[1]+1 if count[1]<b else b+1): dp[1][i]=1 #초기값으로 1만을 고려했을 떄 모든 경우의 수가 1이므로 모든 위치에 1을 넣어준다
for i in range(2,t+1): #2부터 탐색한다
    for j in range(b+1): #주어진 가장 큰 부분 집합의 개수에 대해
        for k in range(j-count[i] if j-count[i]>0 else 0,j+1): #직전 숫자까지 고려한 값을 반영하여 현재 값을 업데이트한다
            dp[i][j]+=dp[i-1][k]
            dp[i][j]=dp[i][j]%M

#for e in dp: print(e)
result = 0
for i in range(s,b+1): #마지막 값까지 고려했을때에 주어진 범위의 값을 모두 더한다
    result+=dp[t][i]
    result=result%M
print(result)
#----------------------------------------------
#문제 분야 : 다이나믹 프로그래밍
#https://www.acmicpc.net/problem/2092
