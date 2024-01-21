
import heapq
import sys
import bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

n = int(input())
lst = list(map(int, input().split()))

lis = [] #빈 리스트 선언

for num in lst:
    #bisect : 해당 리스트에서 특정 값을 삽입할 경우 그 값이 들어갈 인덱스를 구해주는 함수
    i = bisect.bisect_left(lis,num) #현재 값이 들어갈 인덱스를 구한다

    if i==len(lis):
        lis.append(num) #만약 구한 인덱스가 lis의 길이와 같다면 append해주고
    else:
        lis[i]=num #아니라면 해당 인덱스의 값을 업데이트 한다

print(len(lis)) #구한 리스트의 길이를 출력한다

#----------------------------------------------
#문제 분야 : 이분탐색
#https://www.acmicpc.net/problem/2352
