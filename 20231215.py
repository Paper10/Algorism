
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

inputs = list(input().rstrip())
matching = input().rstrip()

l = len(matching)

stack = []

for char in inputs:
    stack.append(char)

    if len(stack) >= l:
        # 마지막 문자열이 matching과 같으면 stack에서 pop한다.
        if ''.join(stack[-l:]) == matching:
            for _ in range(l):
                stack.pop()

ans = ''.join(stack)
if not ans: #답이 없다면 FRULA 출력
    print('FRULA')
else:
    print(ans)

#----------------------------------------------
#문제 분야 : 스택
#https://www.acmicpc.net/problem/9935

