
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
for _ in range(N):
    n = int(input())
    d = 2 #등차수열의 합은 (총 항의 개수) * (중간 값) 으로 나타낼 수 있으므로 n을 2부터 차례로 나누어본다
    result = 0
    while(True):
        tar = n/d
        if d%2==1 and tar-int(tar)==0: #만약 n을 홀수개로 나누었을때 값이 정수라면 만족하는 등차수열이 존재한다는 의미
            if tar-((d-1)/2)<1 : break #해당 등차수열의 가장 작은 값이 1보다 작다면 빠져나오고
            else : result+=1 #아니라면 1을 더한다
        elif d%2==0 and tar-int(tar)==0.5: #만약 n을 짝수개로 나누었을때 값이 0.5로 끝난다면 등차수열이 존재한다는 의미
            if int(tar)-(d/2)+1<1 : break #해당 등차수열의 가장 작은 값이 1보다 작다면 빠져나오고
            else : result+=1#아니라면 1을 더한다
        if d*d>n*4 : break #특정 수 이상으로 넘어가면 break
        else : d+=1 #아니라면 d를 1늘리고 반복한다
    print(result)
#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/2737
