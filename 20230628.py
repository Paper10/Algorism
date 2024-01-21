
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution(n, computers):
    answer = 0
    visit = [False]*n #방문한 노드를 기록하는 배열
    
    def dfs(s):
        visit[s]=True #현재 노드를 방문 처리하고
        for i,e in enumerate(computers[s]):
            if e==1 and not visit[i]: #현재 노드와 연결된 노드 중 방문하지 않은 노드에 대해
                dfs(i) #재귀적으로 함수를 다시 호출한다
    
    for i,b in enumerate(visit): #방문 배열을 탐색하며
        if b : continue #해당 노드를 아직 방문하지 않았다면
        dfs(i) #해당 노드와 연결된 네트워크를 모두 방문처리하고
        answer+=1 #결과에 1을 더한다
    return answer

#----------------------------------------------
#문제 분야 : dfs
#https://school.programmers.co.kr/learn/courses/30/lessons/43162
