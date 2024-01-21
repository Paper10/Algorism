
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
# 동전을 내림차순으로 정렬한다.
coin.sort(reverse=True)
# 동전 개수
count = 0

for i in range(len(coin)):
    # 동전이 K보다 작거나 같으면
    if coin[i] <= k:
        # 동전으로 K를 나눈 몫을 num에 넣는다.
        # 여기서 num(몫)은 개수가 된다.
        num = k // coin[i]
        # num과 동전을 곱해준 값을 k에 빼준다.
        k -= num * coin[i]
        # 개수를 더해준다.
        count += num
    # 가치가 0이 되면 반복문을 멈춰준다.
    if k == 0:
        break

print(count)

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/11047

