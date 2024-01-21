import sys
from collections import deque
input = sys.stdin.readline

sen = input()#중위 표기식을 입력받고
pr = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}#각 연산자의 우선순위를 정해준다
letter = 'x'#저장된 문자가 없는 상태를 x로 정의한다
s = [] #스택 선언
result = [] #결과를 저장할 배열
for e in sen: #입력받은 문자열을 탐색한다
    if e.isupper():#만약 알파벳이라면
        if not letter=='x' : result.append(letter)
        letter = e#기존의 알파벳을 결과에 저장하고 letter 변수에 저장한다
    elif e in pr: #만약 연산자라면
        if not s or e=='(' or s[-1]=='(' or pr[e]>pr[s[-1]]:
            s.append(e) #스택이 비어있거나 ( 문자 혹은 ( 문자 바로 다음이거나 직전 문자의 우선순위가 더 낮으면 스택에 추가한다
        elif not e==')' and pr[e]<=pr[s[-1]]: # ) 문자가 아니고 직전 문자의 우선순위가 저 높으면
            if not letter=='x' : result.append(letter)
            letter = 'x' #저장된 문자열을 결과에 더하고
            while s and pr[e]<=pr[s[-1]]:
                result.append(s.pop())
            s.append(e) #자신보다 낮은 우선순위의 문자가 나올때까지 스택에 저장된 문자를 결과에 더한다
        elif e==')': # ) 문자가 나올경우
            if not letter=='x' : result.append(letter)
            letter = 'x' #저장된 문자를 결과에 더하고
            while s[-1]!='(':
                result.append(s.pop())
            s.pop() # ( 문자가 나올떄까지 스택의 문자를 저장한 후 ( 문자를 스택에서 제거한다
if not letter=='x' : result.append(letter) #루프가 끝난 후 저장된 문자를 결과에 마저 더한다
while s:
    result.append(s.pop()) #문자 또한 다시 더한다

print(''.join(result)) #결과 출력
#----------------------------------------------
#문제 분야 : 스택
#https://www.acmicpc.net/problem/1918