
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def see(bp):
    tilt = INF * (-1) #초기 기울기 값을 음수 무한대로 설정
    count = 0
    for i in range(1,len(bp)): #가장 왼쪽의 노드를 기준으로
        tiltnow = (bp[i]-bp[0])/i 
        if tilt<tiltnow: #현재 탐색중인 노드와의 기울기가 저장된 기울기보다 크다면 건물을 볼 수 있다는 의미이므로
            count+=1
            tilt=tiltnow #개수를 더하고 기울기를 업데이트한다
    return count


n = int(input())
build = list(map(int, input().split()))

result = 0
for i in range(n): #각 노드에 대하여
    tmp = see(build[i:]) + see(build[:i+1][::-1]) #현재 건물에서 오른쪽으로 보이는 건물과 왼쪽으로 보이는 건물을 합한다
    result = max(tmp,result) #최대값 저장

print(result)
#----------------------------------------------
#문제 분야 : 브루트 포스
#https://www.acmicpc.net/problem/1027
