import heapq
import sys
from collections import deque
input = sys.stdin.readline

# 입력부분
board = input()

board = board.replace("XXXX", "AAAA") #먼저 AAAA로 덮을수 있는 부분을 모두 덮는다
board = board.replace("XX", "BB") #그 후 BB로 덮을수 있는 부분을 덮는다

if 'X' in board:
    print(-1) #만약 아직 덮지 못한 곳이 있다면 실패를 출력한다
    
else:
    print(board) #결과 출력

#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/1343