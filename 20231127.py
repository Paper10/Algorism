
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N,K,block = map(int,input().split())
arr = list(map(int,input().split()))+[N+1] #각 구간의 길이를 구하기 위해 총 구간의 길이+1를 추가
last = 0
distance = []
side = []
for i,e in enumerate(arr):
    if i==0 or i==len(arr)-1 : side.append(e-last-1) #첫번째와 마지막 구간은 칸막이 하나로 확보 가능하므로 따로 저장한다
    else : heapq.heappush(distance,1+last-e)#각 구간의 길이를 큰것부터 내림차순으로 힙에 추가한다
    last = e

result=0
while(block>3): #칸막이가 3개보다 많을경우
    if not distance:break #만약 칸막이를 다 쓰지 않았는데 남은 중간 구간이 더 없을 경우 빠져나온다
    result+=(-1)*(heapq.heappop(distance)) #힙에서 가장 큰 원소를 결과에 추가하고
    block-=2 #구간 확보를 위한 칸막이 2개를 삭제한다
if block==1: result+=max(side) #칸막이가 1개 뿐이었을 경우 양 사이드중 하나를 선택한다
elif not distance: result+=sum(side) #칸막이가 2개 이상 남았지만 중간 구간이 더 없을경우 양 사이드를 더한다
elif block==2: result+=max(sum(side),(-1)*distance[0])#칸막이가 2개일 경우 양 사이드의 합과 남은 중간 구간 중 큰 값을 더한다
elif block==3: result+=max(sum(side),(-1)*distance[0]+max(side))#칸막이가 3개일경우 양 사이드의 합과 사이드중 큰값+남은 중간구간 중 큰 값을 더한다

print(result)
#----------------------------------------------
#문제 분야 : 그리디 알고리즘
#https://www.acmicpc.net/problem/11912
