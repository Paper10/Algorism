
import heapq
import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(1000000)

n = int(input())
lst = []
for i in range(n):
    a,b = map(int, input().split()) 
    heapq.heappush(lst,(-b,a)) #받을 수 있는 컵라면의 수를 기준으로 정렬

result = 0
done = [True] + [False]*n
for cup,dead in lst:
    for i in range(dead,0,-1): #현재 노드의 데드라인을 기준으로
        if not done[i]: #할 수 있는 날짜중 가장 늦은 날짜를 true 처리한 후
            done[i]=True
            result-=cup #결과를 더한다
            break


print(result,lst)

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/1781
