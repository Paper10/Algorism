
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

#아파트 단지의 위치와 학생 수를 나타내는 배열을 선언 후 입력받는다
n,k,s = map(int, input().split())
line = [0] * 100001
for _ in range(n):
    a,b = map(int, input().split())
    line[a]=b

#학생이 존재하는 오른쪽 끝과 왼쪽 끝 지점을 l1,l2로 선언 후 초기화 한다
l1 = 0
l2 = 100000
result = 0

while(l1<s or l2>s): #양 끝이 모두 학교 위치일때 멈춘다
    
    #학생이 존재하는 오른쪽 끝의 위치를 찾고 해당 지점까지의 거리 *2 값을 더한다
    for i in range(l1,s+1,1):
        if not line[i]==0:
            l1 = i
            break
        if i==s: l1=s
    result += (s-l1)*2

    #학생이 존재하는 왼쪽 끝의 위치를 찾고 해당 지점까지의 거리 *2 값을 더한다
    for i in range(l2,s-1,-1):
        if not line[i]==0:
            l2 = i
            break
        if i==s: l2=s
    result += (l2-s)*2
        
    #가장 먼 지점에서 부터 학생을 태울 수 있을 만큼 태운다
    tk = k
    for i in range(l1,s+1,1):
        if tk>line[i]:
            tk -= line[i]
            line[i]=0
        else:
            line[i] -= tk
            break

    tk = k
    for i in range(l2,s-1,-1):
        if tk>line[i]:
            #if line[i]!= 0: print(tk,i,line[i],'if')
            tk -= line[i]
            line[i]=0
        else:
            #if line[i]!= 0: print(tk,i,line[i],'else')
            line[i] -= tk
            break
    
    #print(l1,l2,'end')

#결과 출력
print(result)

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/2513
