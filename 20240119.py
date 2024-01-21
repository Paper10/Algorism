
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

n = int(input())
numbers = list(map(int, input().split()))
m = max(numbers)
s = [False,False] + [True]*(m-1) #소수값을 저장할 배열을 선언한다

result = 1 #최대공약수를 저장하는 변수
count = 0 #연산을 수행하는 횟수를 저장하는 변수

for i in range(2,m+1):
    if s[i]: #만약 소수값 배열의 해당 인덱스가 true값이라면
        for j in range(i,m+1,i):s[j]=False #현재 소수값의 배수를 전부 false로 한다
        com = [0 for _ in range(n)]
        for j in range(n):
            while(numbers[j]%i==0): #현재 소수값으로 입력값을 최대한 나누고
                numbers[j]/=i
                com[j]+=1 #나눈 횟수를 저장한다
        comr = sum(com)//n #현재값이 나눠진 횟수의 합을 입력값의 개수만큼 나누고 몫을 구한다
        for _ in range(comr): result*=i 
        for e in com:
            if comr>e: count+=comr-e #구한 몫으로 옮기는 횟수와 결과를 저장한다
print(result,count)


        

#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/2904
