
import heapq
import sys
from collections import deque
input = sys.stdin.readline

def solution(money):
    
    # 입력된 일직선의 집들 중에서 최대의 돈을 가져가는 함수
    def rob(m):
        n = len(m)
        dp = [0] * n
        dp[0] = m[0] #첫번째 집의 경우 자신의 소유금이 최대
        dp[1] = max(m[0],m[1]) #두번쨰 집의 경우 첫번쨰 집과 두번쨰 집중 더 큰 금액이 최대
        
        for i in range(2, n): # 이후의 집에대해
            dp[i] = max(dp[i-1], dp[i-2] + m[i]) #바로 이전 집의 금액과 전전 집의 금액 + 현재 집의 금액중 큰 값이 최대
        
        return dp[-1] #마지막 집의 값이 해당 배열에서 가능한 최대 금액
    
    #주어진 집들이 원형이므로 첫번쨰 집을 제외하거나 마지막 집을 제외한 결과 중 큰 값이 원형에서의 최댓값
    answer = max(rob(money[1:]), rob(money[:-1]))
    return answer


#----------------------------------------------
#문제 분야 : 다이나믹 프로그래밍
#https://school.programmers.co.kr/learn/courses/30/lessons/42897
