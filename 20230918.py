import heapq
import sys
from collections import deque
input = sys.stdin.readline

# 입력
n,m = map(int, input().split())
lst = [[] for _ in range(n)]
for _ in range(n):
    arr = list(map(int, input().split()))
    for i in range(n):
        lst[i].append(arr[i]) # 세로열 입력
    lst.append(arr) # 가로열 입력

result = 0 #출력할 결과값을 초기화한다
for e in lst: #리스트의 모든 원소를 탐색한다
    e2 = e[:] #계단의 설치여부를 확인하기 위한 복사배열을 만들어준다
    check = True # 올바른 길인지 확인할 변수를 만든다
    for i in range(n-1): # 길을 탐색하면서 자신과 바로 다음 인덱스의 원소를 비교한다
        if e[i]==e[i+1]: # 만약 높이가 같다면 지나간다
            continue
        elif e[i]==e[i+1]+1: #만약 다음 길의 높이가 1 낮다면
            t = e[i+1] # 다음 길의 높이를 저장하고
            for ni in range(i+1,i+1+m): # 계단 길이만큼 탐색하면서 계단을 놓을수 있는 같은 높이인지 확인한다
                if ni>=n or e[ni]!=t: check=False # 만약 범위를 넘어가거나 높이가 달라진다면 확인하는 변수를 False로 한다
                else : e2[ni] = -e[ni] #만약 계단을 놓을수있는 위치라면 복사한 배열의 해당 인덱스를 -로 바꿔준다
        elif e[i]==e[i+1]-1: #만약 다음 길의 높이가 1 높다면
            t = e[i] #현재 길의 높이를 저장하고
            for ni in range(i,i-m,-1): #계단 길이만큼 반대로 탐색하며 게단을 놓을수있는지 확인한다
                if ni<0 or e2[ni]!=t : check=False  #이때 복사한 배열을 탐색하면 이미 계단이 놓아진 부분은 부호가 바뀌어 있어 놓을수 없는 위치로 판단할 수 있다
        else: check=False #만약 높이가 2이상 차이나면 올바르지 않은 길이다
    if check : result += 1 # 만약 올바른 길이라면 결과에 1을 더한다
print(result)

#----------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/14890