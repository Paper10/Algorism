
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution(s):
    answer = ''
    arr = list(map(int, s.split())) # 입력된 문자열을 정수배열로 변환
    answer = str(min(arr)) + ' ' + str(max(arr)) #최소값과 최대값을 저장
    return answer

#----------------------------------------------
#문제 분야 : 구현
#https://school.programmers.co.kr/learn/courses/30/lessons/12939
