
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution(n):
    global answer
    answer = 0
    
    def find(a,b): #남은 '(' 개수와 ')'개수를 a,b로 입력받는다
        global answer
        if a==0 : answer+=1 #만약 더이상 '('개수가 없을경우 뒷부분이 전부 ')'이므로 결과에 1을 더하고 종료한다
        elif a==b : find(a-1,b) #만약 두 '('개수와 ')'개수가 같을 경우 ')'를 사용할 수 없으므로 '('를 사용한다
        else: #그 외의 경우에 대해
            find(a-1,b) #'('를 사용한 경우와
            find(a,b-1) #')'를 사용한 경우를 재귀적으로 호출한다
    find(n,n)
    return answer

#----------------------------------------------
#문제 분야 : 재귀 
#https://school.programmers.co.kr/learn/courses/30/lessons/12929
