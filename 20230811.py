
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def makedic(a):
    A = [0] + a[:]
    
    for i in range(1,len(A)): A[i]+=A[i-1] #입력받은 배열을 누적합 배열로 변환한 뒤
    
    dA = {}
    for i in range(1,len(A)):
        for j in range(i):
            tmp = A[i]-A[j] #위치 j의 누적합에서 위치 i의 누적합을 빼면 위치 i~j를 가지는 부배열의 합이 되므로
            if tmp in dA: dA[tmp]+=1
            else: dA[tmp]=1 #해당 부 배열의 합을 딕셔너리에 저장한다
    
    return dA

#입력
t = int(input())
lenA = int(input())
A = list(map(int, input().split()))
lenB = int(input())
B = list(map(int, input().split()))

#각 배열의 부 배열들의 원소의 합의 개수를 저장하는 딕셔너리를 만든다
dA = makedic(A)
dB = makedic(B)

result = 0
for a in dA: #A 배열의 모든 원소에 대해
    if t-a in dB: result+=dA[a]*dB[t-a] #B 배열의 원소중 합이 t가되는 원소가 있다면 개수를 곱한만큼 결과에 더한다
print(result)

#----------------------------------------------
#문제 분야 : 누적합
#https://www.acmicpc.net/problem/2143
