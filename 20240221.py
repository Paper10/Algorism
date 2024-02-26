
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def lower(arr,t): #이분 탐색을 활용하여 탐색중인 수가 들어갈 인덱스를 리턴한다
    mid = 0
    s = 0
    e = len(arr)
    while(e-s>0):
        mid = (s + e)//2
        if arr[mid]>t: s=mid+1
        else: e=mid
    return e-1

n = int(input())
lst = list(map(int, input().split()))

lw = []
for e in lst:
    if not lw: lw = [e]
    elif e>lw[0]: lw = [e]+lw #만약 lw가 비어있거나 현재 탐색중인 수보다 작은수가 0번 인덱스에 있다면 추가
    else: lw[lower(lw,e)] = e #아니라면 해당하는 위치에 삽입한다
print(n-len(lw)) #전체 개수에서 lw배열의 길이를 뻬면 실행해야 하는 행동 횟수가 나온다

#----------------------------------------------
#문제 분야 : 이분 탐색
#https://www.acmicpc.net/problem/1818
