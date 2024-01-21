
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution(k, room_number):
    answer = []
    room = {} #이미 배정된 방을 저장할 딕셔너리
    
    def find(n): #함수의 인자로 받은 방 번호에 대해
        if not n in room: #만약 배정되지 않은 방일 경우
            room[n]=n+1 #딕셔너리에 해당 방을 추가하고 다음 방을 안내하도록 설정
            return n
        else: #만약 배정받은 방일 경우
            room[n] = find(room[n]) #해당 방을 안내받았을 경우 다음으로 안내받는 방을 재귀적으로 호출하여 업데이트
            return room[n] #업데이트 된 방을 반환
        
    for e in room_number:
        answer.append(find(e))
    return answer
#----------------------------------------------
#문제 분야 : 재귀
#https://school.programmers.co.kr/learn/courses/30/lessons/64063
