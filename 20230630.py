
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution(words):
    global answer
    answer = 0

    def div(ar):#재귀적으로 문자열을 탐색하며 같은 문자로 시작하는 문자열들을 분류하는 함수
        global answer
        arr = sorted(ar[:]) #문자열들이 abc순으로 정렬할수 있도록 전체정렬
        if arr[0]=='' : arr=arr[1:] #만약 문자열의 첫번쨰 문자가 빈문자열이라면 제거
        tmp = arr[0][0]
        nxt_arr = [] #같은 문자로 시작하는 문자열들을 저장할 임시 배열
        for i,e in enumerate(arr): #입력된 문자열을 돌면서
            if e[0]==tmp: #같은 문자열로 시작할 동안 임시 배열에 첫번쨰 문자를 제외하고 추가하며
                nxt_arr.append(e[1:])
            else: #더이상 같은 문자로 시작하는 문자열이 없으면 지금까지 저장된 문자열들이 같은 문자로 시작했던 문자열들이란 뜻이므로
                answer += len(nxt_arr) #해당 문자열의 길이를 더하고
                if len(nxt_arr)>1 : div(nxt_arr) #만약 문자열 집합의 길이가 1이라면 더이상 분석할 필요가 없으므로 스킵한다
                nxt_arr = [e[1:]] 
                tmp = arr[i][0]#다음 문자로 시작하는 문자열을 받을 준비를 한다
        answer += len(nxt_arr)
        if len(nxt_arr)>1 : div(nxt_arr)
        
    div(words)
        
    return answer
#----------------------------------------------
#문제 분야 : 재귀
#https://school.programmers.co.kr/learn/courses/30/lessons/17685
