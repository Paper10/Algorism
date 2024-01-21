
import heapq
import sys
from collections import deque
input = sys.stdin.readline

#입력 부분
n = int(input())
if n==0 : #0 입력시 실패
    print("NO")
    exit() 

fact = [1] #팩토리얼을 저장할 배열
i = 1 # 1! 부터 시작
while True:
    now = 1
    for k in range(1,i+1):
        now *= k # i!을 구한 후
    if now > n: break # 만약 값이 입력된 n 보다 크다면 그만하고
    else:
        fact.append(now) #아니라면 배열에 저장한뒤
        i += 1 # 다음 팩토리얼을 구한다

while fact and n>0: #만약 팩토리얼 배열에 원소가 남아있고 n값도 0보다 크다면
    f = fact.pop() #팩토리얼 배열에서 가장 큰 값을 뽑아
    if n>=f : n-=f #만약 그 값이 n보다 크다면 빼준다
    
if n==0: print("YES") #만약 결과가 0으로 떨어졌다면 YES를
else: print("NO") #아니라면 NO를 출력한다
#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/2057
