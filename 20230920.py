import heapq
import sys
from collections import deque
input = sys.stdin.readline

#입력된 정수의 생성자를 알려주는 함수
def make(n):
    tmp = n
    result = n # 결과에 n을 저장하고
    while tmp>0:
        result += tmp%10 #각 자리숫자를 더한다
        tmp = tmp//10
    return result

target = [True] * 10001 #1부터 10000까지의 배열을 생성한 후
for i in range(1,10001): #10000까지 탐색하면서
    if target[i] : print(i) #만약 생성자가 아닐경우 출력하고
    target[make(i) if make(i)<=10000 else 2] = False #현재 탐색중인 정수의 생성자에 해당하는 인덱스의 원소를 False로 한다

#------------------------------------------------------------
#문제 분야 : 브루트 포스
#https://www.acmicpc.net/problem/4673