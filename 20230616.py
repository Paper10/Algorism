import heapq
import sys
from collections import deque
input = sys.stdin.readline

# 입력부분
n = int(input())

#n이 1일경우 0 출력
if n == 1:
    print(0)
    exit()

# 소수 리스트 생성부분
check = [True] * (n+1) # n+1 길이의 배열 생성
check[0],check[1] = False,False # 0,1의 경우 예외 처리
lst = [] # 소수를 넣을 배열 생성
for i in range(n+1): # n까지 탐색하면서
    if check[i]: # 만약 check 배열의 해당 인덱스의 값이 True 라면
        lst.append(i) # 소수 리스트에 넣고
        for j in range(i,n+1,i): # 해당 인덱스의 배수를 가지는 모든 인덱스를
            check[j]=False #false 값으로 바꾼다

q = deque()
q.append(0) # 소수 리스트의 인덱스를 담아둘 큐를 생성 후 초기값인 0을 넣어준다
sum = 2 # 모든 소수의 합을 저장할 변수에 소수리스트의 첫 원소인 2를 넣어준다
result = 0 # 출력값
while True:
    if sum>n: #만약 소수의 합이 n보다 커지면
        sum -= lst[q.popleft()] # 큐의 원소중 가장 작은값을 큐에서 제거하고 sum 값에서 해당 인덱스의 소수값을 뺸다
    elif sum<=n: # 만약 소수의 합이 n보다 작다면
        if sum==n: #만약 두 값이 같다면
            result += 1 # 결과에 1을 더하고
            #print(q,"ok")
        tmp = q[-1]+1 
        if tmp==len(lst) : break # 만약 다음 소수가 없다면 반복을 빠져나온다
        sum += lst[tmp] 
        q.append(tmp) #다음 소수에 해당하는 인덱스를 큐에 넣고 sum값에 해당 소수를 더한다
print(result)

#----------------------------------
#문제 분야 : 소수
#https://www.acmicpc.net/problem/1644