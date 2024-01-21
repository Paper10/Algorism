import heapq
import sys
from collections import deque
input = sys.stdin.readline

#입력
n,k = map(int, input().split())
tab = [-1]*n
s = list(map(int, input().split()))

result = 0
for i in range(k):
    if s[i] in tab : continue #만약 이미 멀티탭에 들어있다면 넘어간다
    elif -1 in tab : tab[tab.index(-1)] = s[i] #만약 멀티탭에 빈자리가 있을경우 넣는다
    else:
        result += 1
        use = [True] * n #현재 멀티탭의 전자기기중 이후에 사용할 전자기기를 체크하기 위한 배열
        tar = 0
        for j in range(i+1,k): # 현재 탐색중인 인덱스 이후의 원소들에 대해
            if s[j] in tab: #만약 사용한다면
                use[tab.index(s[j])] = False # use 배열의 해당 인덱스를 false로 바꾸고
                tar = tab.index(s[j]) #해당 인덱스를 저장한다
        if True in use: #만약 이후에 사용할 예정이 없는 전자기기가 있다면
            tab[use.index(True)]=s[i] #해당 위치를 교체한다
        else:
            tab[tar]=s[i] # 마지막에 저장된 인덱스의 위치를 교체한다
    print(tab,i,result)
print(result)

#-------------------------------------------------
#문제 분야 : 그리디
#https://www.acmicpc.net/problem/1700