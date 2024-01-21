import heapq
import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
paper = [[True]*101 for _ in range(101)] #전체 종이의 면적을 나타내는 배열을 선언한다

result = 0
for _ in range(num):
    n,m = map(int,input().split())
    for i in range(n,n+10):
        for j in range(m,m+10):
            if paper[i][j]: #만약 탐색중인 부분이 아직 덮이지 않은 부분이라면
                result += 1 # 결과값에 1을 더하고
                paper[i][j]=False # 해당 부분을 덮은 부분으로 처리한다

print(result)
#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/2563