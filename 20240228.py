
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

def find(arr, t): #이분탐색을 사용하여 배열에서 t값보다 작은 수 중 가장 큰 값의 인덱스를 반환
    s = -1
    e = len(arr)-1
    result = -1
    while s<e:
        mid = (s+e+1)//2
        if arr[mid]<t:
            result = mid
            s=mid
        else: e=mid-1
    return result

n = int(input())

lst = []
num = {0:[]} #각 색깔 마다 공의 크기를 저장하는 배열, 0번 항목은 공 전체를 모두 입력받는다
for _ in range(n):
    a,b = map(int, input().split())
    lst.append((a,b))
    num[0].append(b)
    if a in num: num[a].append(b)
    else: num[a]=[b]

hum = {} #각 색깔 별 누적합을 저장하는 배열
for a in num:
    num[a].sort() #배열을 크기순으로 정렬하고
    hum[a] = [] #누적 합 배열을 생성한다
    t = 0
    for e in num[a]:
        t += e
        hum[a].append(t)

#print(num,hum)

for c,s in lst: #각 공에 대해
    f0 = find(num[0], s) #전체 공 배열에서의 알맞은 인덱스를 찾고
    f0 = 0 if f0==-1 else hum[0][f0] #해당 인덱스의 누적합 저장, 만약 함수가 -1을 반환한다면 가장 작은 수라는 의미이기 때문에 0값을 저장
    fc = find(num[c], s)
    fc = 0 if fc==-1 else hum[c][fc] #현재 공과 같은 색깔에 대해서도 같은 과정 반복

    #print(f0,fc)
    print(f0-fc) #전체 공의 누적합에서 현재 공과 동일한 색의 누적합을 뺀 후 출력

#----------------------------------------------
#문제 분야 : 누적합
#https://www.acmicpc.net/problem/10800
