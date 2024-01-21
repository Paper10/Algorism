import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
for _ in range(N):
    a,b = map(int, input().split())
    n = a+b #입력된 두 끈의 합을 저장한다
    
    s = [False,False]+([True] * (n-1))
    for i in range(2,n+1):
        if s[i] :
            for j in range(i*2,n+1,i) : s[j]=False #소수의 배수는 소수가 아니므로 이를 이용하여 소수만 남긴다
    
    check = True
    for i in range(2,(int)((n+3)/2)):
        if s[i] and s[n-i] : #만약 소수와 n-소수 값이 전부 소수라면
            print("YES") #YES를 출력하고
            check = False
            break
    if check : print("NO") #아니라면 NO를 출력한다

#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/15711
