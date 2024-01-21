
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def cal(a,b,o):
    if o==0 : return a+b
    if o==1 : return a-b
    if o==2 : return a*b
    if o==3 :
        div = True 
        return a/b if not b==0 else 0

n = int(input())
order = [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)] #연산을 수행할 수의 순서와
oper = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            oper.append((i,j,k)) #연산자의 순서를 모두 정의한다

for _ in range(n):
    a = list(map(int, input().split())) #정수를 입력받고
    
    check = False
    for d1,d2,d3 in order:
        for o1,o2,o3 in oper: #모든 조합에 대해 계산을 수행하여
            div = False #0으로 나누는 경우를 예외처리
            ar = a[:]
            ar[d1-1]=cal(ar[d1-1],ar[d1],o1)
            ar.pop(d1)
            if d2>d3:
                ar[1]=cal(ar[1],ar[2],o2)
                ar[0]=cal(ar[0],ar[1],o3)
            else:
                ar[0]=cal(ar[0],ar[1],o2)
                ar[1]=cal(ar[1],ar[2],o3)
            if div : continue

            if ar[0]==24: #만약 현재 조합이 24를 만들 수 있다면
                check=True
                break
        if check : break
    if check : print("YES") #YES를 출력한다
    else : print("NO")
#----------------------------------------------
#문제 분야 : 브루트 포스
#https://www.acmicpc.net/problem/9320
