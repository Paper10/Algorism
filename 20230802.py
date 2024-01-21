
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
lst = list(map(int, input().split()))
stick = []
for e in lst: heapq.heappush(stick, (-1)*e) #입력받은 막대들을 힙에 내림차순으로 삽입한다

result = 0
square = []
m = 0 #직전의 막대를 저장할 변수
while(stick):
    n = heapq.heappop(stick) #힙에서 원소를 pop하고
    
    if m==n or m+1==n: #만약 직전의 막대와 같거나 1차이 라면
        square.append((-1)*n) #사각형 배열에 추가하고
        m = 0 #직전 배열을 초기화 한다
    else:
        m = n #아니라면 직전 배열을 업데이트 한다

    if len(square)==2: #만약 사각형 배열에 원소가 2개일 경우
        result += square[0]*square[1] #결과에 사각형의 넓이를 더하고
        square = [] #초기화한다

print(result)

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/2248
