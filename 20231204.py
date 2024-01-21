
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

word = {} # 나무의 종류
n = 0 # 나무의 개수

# 반복문을 통해 나무를 입력받는다.
while True:
    tree = str(sys.stdin.readline().rstrip())

    # 입력받은 나무가 없다면 반복문을 멈춘다.
    if not tree:
        break

    # 나무의 종류에 이미 나무가 있다면 카운트
    if tree in word:
        word[tree] += 1

    # 나무의 종류에 나무가 없다면 나무를 추가
    else:
        word[tree] = 1

    n += 1 # 나무의 개수 카운트

# 사전순으로 정렬해주기 위해 나무의 종류를 리스트로 만든다.
trees = list(word.keys())
trees.sort() # 오름차순으로 정렬

# 사전순으로 정렬한 나무의 이름순으로 백분율을 계산해 출력
for j in trees:
    print("%s %.4f" % (j, word[j] / n * 100))

#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/4358

