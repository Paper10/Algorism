
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

num = {2:'1', 3:'7', 4:'4', 5:'2', 6:'6', 7:'8', 8:'10', 10:'22', 11:'20', 17:'200'} #남은 성냥개비에 따라 만들 수 있는 가장 작은 수
N = int(input())
for _ in range(N):
    
    o = int(input())
    max_ = '7' * (o%2) + '1' * ((o//2) - (o%2)) #1을 최대한 사용한 후 만약 3개가 남을떄는 7을 붙이는 방법이 가장 큰 수
    min_ = ''

    n = o
    while(True):
        if n in num: #만약 num배열에 남은 성냥개비 개수가 존재한다면 사용 후 종료
            min_ = num[n] + min_
            break
        min_ = '8' + min_ #8을 최대한 사용하여 성냥개비 개수를 줄인다
        n -= 7

    print(min_ + ' ' + max_)
        


#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/2437
