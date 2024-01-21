
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def makedict(word): #단어가 입력되면 알파벳 구성을 담은 딕셔너리를 반환
    newdict = {}
    for e in word:
        if e in newdict : newdict[e]+=1
        else : newdict[e]=1
    return newdict

def adddict(dict,char): #입력된 딕셔너리에 입력된 문자를 추가
    newdict = dict
    if char in newdict : newdict[char]+=1 #만약 이미 존재하는 알파벳이면 1을 더하고
    else : newdict[char]=1 #아니라면 새 원소를 만든다
    return newdict

def find(sen,cost):
    #print(sen,cost)
    global Cost
    if not sen : #만약 문장이 빈 문장이라면 원문의 끝까지 도달한것이므로
        Cost = cost if Cost>cost else Cost #지금까지의 값을 저장한다
        return

    arr = {} #딕셔너리를 선언하고
    for i,e in enumerate(sen):
        arr=adddict(arr,e) #주어진 문장의 구성 알파벳을 딕셔너리에 저장하며
        if arr in sets: #만약 지금까지의 딕셔너리 구성이 주어진 단어들의 딕셔너리 구성과 같다면
            c = 100
            for w in [word[index] for index,value in enumerate(sets) if value==arr]: #해당 딕셔너리 구성을 가지는 모든 단어에 대해
                cc = 0
                for idx in range(len(w)):
                    if not sen[idx]==w[idx] : cc+=1 #규칙에 따라 값을 계산하고
                c = cc if cc<c else c
            find(sen[i+1:] if i+1<len(sen) else "",cost+c) # 지금 탐색중인 문자 다음 문자부터 시작되는 문장과 추가된 값으로 find를 재귀적으로 호출한다



sentence = input()
n = int(input())
sets = []
word = []
for _ in range(n):
    w = input()[:-1] #입력된 문자들에 대해
    word.append(w) #word에 저장하고
    sets.append(makedict(w)) #같은 인덱스에 해당 단어의 구성 알파벳을 저장한다
#print(sets,word)

global Cost
Cost = 100
find(sentence[:-1],0) #find 함수를 실행하여 값을 구한다
print(-1 if Cost==100 else Cost)

#----------------------------------------------
#문제 분야 : 다이나믹 프로그래밍
#https://www.acmicpc.net/problem/1099
