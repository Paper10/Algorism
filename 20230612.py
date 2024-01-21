import sys
from collections import deque
input = sys.stdin.readline

#n,m을 입력받는다
n,m = map(int, input().split())

#자신보다 앞에서는 학생들을 기록한 start, 자신보다 뒤에서야하는 인원수를 기록한 end를 생성한다
start = [[] for _ in range(n+1)]
end = [0 for _ in range(n+1)]

#입력을 받을떄마다 start와 end에 기록한다
for _ in range(m):
    a,b = map(int, input().split())
    start[a].append(b)
    end[b] += 1

#큐를 생성하고 초기값으로 뒤에서야하는 인원수가 없는 학생들을 넣는다
q = deque()
for i in range(1,n+1):
     if end[i]==0:
          q.append(i)
    
while q: #큐에 원소가 존재할동안
     now = q.popleft()
     print(now, end=" ")#큐에서 원소를 꺼내 출력한다
     for e in start[now]:#해당 학생보다 앞에서는 학생들을 기준으로
          end[e] -= 1#자신이 이미 줄을 섰으므로 해당학생의 뒤에서는 학생수를 1 빼준다
          if end[e]==0:#만약 해당 학생의 뒤에서는 학생이 더이상 없다면
               q.append(e)#큐에 해당 학생을 인풋한다

#-----------------------------------------------------------
#문제 분야 : 위상정렬
#https://www.acmicpc.net/problem/2252