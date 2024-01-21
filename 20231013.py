
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def solution(strs, t):
    memo = {}  # 중복 계산을 피하기 위한 메모이제이션을 위한 딕셔너리

    def find(arr):
        if arr in memo:  # 이미 계산된 값이 있는 경우 바로 반환
            return memo[arr]

        if arr in strs:  # 목표 문자열에 포함되는 경우 1 반환
            memo[arr] = 1
            return 1

        min_count = float('inf')  # 최소값을 찾기 위해 무한대로 초기화

        for i in range(1, len(arr) + 1):
            suffix = arr[-i:]  # 문자열 끝에서부터 접두사를 추출
            if suffix in strs:
                prefix = arr[:len(arr) - i]  # 접두사 이전 부분
                count = find(prefix)  # 접두사 이전 부분에서의 최소값 계산
                if count != 0:
                    min_count = min(min_count, 1 + count)

        if min_count == float('inf'):  # 접두사 이전 부분에서의 최소값을 찾지 못한 경우
            memo[arr] = 0
        else:
            memo[arr] = min_count

        return memo[arr]

    answer = find(t)
    return answer if answer != 0 else -1


'''
def solution(strs, t):
    answer = 0

    def find(arr):
        if arr in strs : return 1
        tmp = []
        for i in range(len(arr)):
            if arr[i:] in strs:
                x = find(arr[:i])
                if x!=0 : tmp.append(1+x)
        #print(tmp)
        if tmp : return min(tmp)
        else : return 0
    
    answer = find(t)
    
    return answer if answer!=0 else -1
'''

#----------------------------------------------
#문제 분야 : 
#
