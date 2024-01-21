
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def solution(A, B):
    
    ans = 0
    A.sort()
    B.sort() #A,B정렬
    ia = 0
    for ib in range(len(B)):
        if A[ia]<B[ib]: #만약 B의 최소값이 더 크다면
            ans+=1 #결과에 1을 더하고
            ia+=1 #A의 인덱스를 1증가시킨다
            
    return ans

#----------------------------------------------
# : 
#
