
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(1000000000)

X=9876754321

def match(k):
    if not dp[k]==0 : return dp[k] #dp배열에 존재하는 값이면 그대로 리턴
    sum = 0
    for i in range(0,k-1,2): #기준점에서 2칸 간격으로 선을 긋고
        sum += match(i) * match(k-2-i) #양쪽의 점들의 집합으로 만들 수 있는 조합을 곱한 후 더함
    dp[k]=sum%X #해당 값을 dp에 저장
    return sum


n = int(input())
dp = [0]*(n+1)
dp[0]=1
dp[2]=1 #dp배열의 초기값을 저장
print(match(n)%X)

#----------------------------------------------
#문제 분야 : 다이나믹 프로그래밍
#https://www.acmicpc.net/problem/17268
