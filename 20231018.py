
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
task = [] #과제의 마감 날짜와 점수를 저장할 배열
for _ in range(n):
    a,b = map(int, input().split())
    task.append((b,a)) # (점수,마감날짜) 형식으로 저장한 뒤
task.sort()# 점수순으로 오름차순 정렬한다

done = [True] * 1001 #해당 날짜에 과제를 했는지 알려주는 배열
total = 0 #전체 점수배열
while(task): #전체 과제들을 돌면서
    pow,date = task.pop() #가장 점수가 높은 과제를 pop하고
    while(date>0):
        if done[date] : #만약 마감날짜에 진행할 과제가 없다면
            total += pow
            done[date]=False
            break #해당 과제를 수행하고 해당 날짜의 과제 실행 여부를 False값으로 바꾼다
        else : date-=1 #만약 해당 날짜에 이미 과제를 했다면 그 전날의 과제 여부를 검사한다

print(total)

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/13904
