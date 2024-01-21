import heapq
import sys
from collections import deque
sys.setrecursionlimit(10000)

def func(mid,c): #기준점과 배열이 주어진다
    o = mid-1 
    t = mid # 첫째와 둘째에게 나눠줄 쿠키 바구니 각각의 경계의 초기값을 설정하고
    one = c[o]
    two = c[t] #첫째와 둘쨰가 가져가는 쿠키의 총 합의 초기값을 설정한다
    answer = 0
    while(True):
        if one==two and one>answer : answer=one #만약 두 형제가 가져가는 쿠키의 값이 같다면 answer 에 저장
        if one>=two: #만약 첫쨰의 몫이 둘째보다 클때
            if t==len(c)-1 : return answer #이미 둘째가 가져갈 수 있는 한계에 다다르면 저장된 answer를 리턴
            else : 
                t+=1
                two+=c[t] #아니라면 다음 바구니를 가져가고 경계를 늘린다
        elif one<two: #만약 둘째의 몫이 더 크다면
            if o==0 : return answer #더 이상 못 가져갈 떄 answer를 리턴
            else : 
                o-=1
                one+=c[o] #아니라면 하나 더 가져간다


def solution(cookie):
    answer = 0
    
    for i in range(1,len(cookie)): #배열의 모든 기준점에 대해 함수를 실행한다
        tmp = func(i,cookie)
        if tmp>answer : answer=tmp
    
    return answer

#----------------------------------------------
#문제 분야 : 구현
#https://school.programmers.co.kr/learn/courses/30/lessons/49995
