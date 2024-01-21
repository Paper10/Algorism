
import sys
from collections import Counter
from itertools import combinations
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)


n = int(input())
road = input()[:-1]
result = 0 #결과를 저장할 변수
patern = [1]+[0]*80 # 각 문자가 포함된 개수를 3진수 꼴로 바꿔 표시했을때 해당 수가 지금까지 몇번 나타났는지 저장한다
total = {'T':0, 'G':0,'F':0,'P':0,} #누적 합을 저장할 딕셔너리
for e in road: #각 문자를 순회하며
    total[e] = (total[e]+1)%3 #누적 합의 값을 업데이트 하고
    target = total['T']*27 + total['G']*9 + total['F']*3 + total['P'] #문자의 개수를 3진수로 변환한다
    result+=patern[target] #지금까지 같은 3진수가 나타난 적이 있다면 해당 시점의 문자부터 현재 문자까지의 개수는 모든 문자가 3의 배수 개수라는 뜻
    patern[target]+=1 #현재 3진수의 값을 1 더한다
print(result)

#----------------------------------------------
#문제 분야 : 누적 합
#https://www.acmicpc.net/problem/24548
