import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

for _ in range(3):
    n = int(input())
    check = True
    coin = [] #동전의 금액과 개수를 저장하는 배열
    total = 0
    for _ in range(n):
        a,b = map(int, input().split())
        coin.append((a,b))
        total += a*b
    coin.sort() #낮은 금액부터 표시되도록 정렬
    
    total = (int)(total/2) #전체 금액의 반을 구한 후
    dp = [False]*(total+1) # 특정 금액이 주어진 동전으로 표현 가능한지 판별하는 배열
    dp[0]=True #0원은 항상 가능
    for val,num in coin:
        for _ in range(num): #동전의 개수만큼 반복
            for i in range(total,val-1,-1):
                if dp[i-val] : dp[i]=True #현재 금액보다 지금 탐색중인 동전의 금액만큼 모자란 금액이 가능한 금액이라면
    print(int(dp[total])) #해당 금액도 가능한 금액이다

#----------------------------------------------
#문제 분야 : 다이나믹 프로그래밍
#https://www.acmicpc.net/problem/1943
