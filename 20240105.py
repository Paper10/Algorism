
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

#입력
n = int(input())
lst = list(map(int, input().split()))

#원소의 등장 빈도수를 저장하는 딕셔너리 생성
dic = {}
for e in lst:
    if e in dic: dic[e]+=1
    else: dic[e]=1

#결과값을 저장할 배열과 스택을 구현할 배열을 선언
result = []
stack = []

for e in lst[::-1]: #입력된 배열을 역순으로 돌면서
    while(True):
        if not stack: #스택이 비었을 경우 -1 출력
            result.append(-1)
            stack.append(e)
            break
        elif dic[e]<dic[stack[-1]]: #만약 스택의 다음 데이터가 현재 데이터보다 많이 등장한 경우 스택의 다음 데이터 출력
            result.append(stack[-1])
            stack.append(e)
            break
        else:
            stack.pop() #만약 현재 데이터가 더 많이 등장한 경우 스택에서 데이터 제거

for e in result[::-1]: print(e, end=" ")

#----------------------------------------------
#문제 분야 : 스택
#https://www.acmicpc.net/problem/17299
