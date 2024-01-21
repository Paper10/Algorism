
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def work(arr):
    if dp[member[0]][member[1]][member[2]][M[arr[-1]]][M[arr[-2]]]: return
    else: dp[member[0]][member[1]][member[2]][M[arr[-1]]][M[arr[-2]]]=True #먼저 dp 배열에서 현재상태에서 함수가 진행했는지 확인한다
    if member==[0,0,0]: #만약 모든 문자를 사용했다면 현재 문자열을 출력하고 코드를 종료한다
        print(arr[2:])
        exit()
    if arr[-2]!='C' and arr[-1]!='C' and member[2]>0: #C,B,A 순서대로 주어진 조건이 맞다면 재귀적으로 함수를 호출한다
        member[2]-=1
        work(arr+'C')
        member[2]+=1
    if arr[-1]!='B' and member[1]>0:
        member[1]-=1
        work(arr+'B')
        member[1]+=1
    if member[0]>0:
        member[0]-=1
        work(arr+'A')
        member[0]+=1
    

a = input()[:-1]
member = [0,0,0]
M = {'A':0,'B':1,'C':2,}
for e in a: #입력된 배열에 포함된 문자의 개수를 저장한다
    if e=='A': member[0]+=1
    if e=='B': member[1]+=1
    if e=='C': member[2]+=1

dp = [] #A,B,C의 개수, 전 문자, 전전 문자의 상태에서 연산을 실행했는지 여부를 저장하는 5차원 배열을 선언한다
for _ in range(member[0]+1):
    i1 = []
    for _ in range(member[1]+1):
        i2 = []
        for _ in range(member[2]+1):
            i3 = []
            for _ in range(3):
                i4 = []
                for _ in range(3):
                    i5 = False
                    i4.append(i5)
                i3.append(i4)
            i2.append(i3)
        i1.append(i2)
    dp.append(i1)

work('AA') #전전 문자가 존재한다는 가정 하에 동작하는 함수이므로 초기값 'AA'를 넣어준다
print('-1') #만약 함수에서 출력이 이루어지지 않았다면 -1 출력

#----------------------------------------------
#문제 분야 : dp
#https://www.acmicpc.net/problem/14238
