
import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,final = map(int, input().split())

start = [] #각 역주행 구간의 시작점들을 저장할 힙
end = [] #각 역주행 구간의 끝점들을 저장할 힙
for _ in range(n):
    b,a = map(int, input().split())
    if a>=b : continue #정방향 구간의 경우 목적지까지 이동하면서 무조건 손님이 이동 가능하므로 무시
    heapq.heappush(start,a) 
    heapq.heappush(end,b) #역주행 구간의 시작점과 끝점을 각각 저장

result = final #목적지까지 이동해야 하므로 초기값을 목적지로 한다
s_point = -1
e_point = -1 #역주행 구간의 시작점과 끝점을 저장할 변수
count = 0
while(end):
    if s_point == -1: #만약 저장된 구간이 없다면 시작점 힙의 첫 원소를 저장
        s_point = heapq.heappop(start)
        count += 1 #그 후 카운터를 1 늘린다
    elif not start or start[0]>end[0]: #각 힙의 첫 원소를 비교하여 더이상의 시작점이 없거나 시작점 중 가장 작은 원소가 끝점보다 클때
        e_point = heapq.heappop(end) #끝점을 저장하고
        count -= 1 #카운터를 1 감소시킨다
        if count==0: #카운터가 0이라는 의미는 같은 개수의 시작점과 끝점을 지났다는 말이므로 현재 저장된 양 끝점이 역주행 구간이라는 뜻이된다
            result += 2*(e_point-s_point) #역주행 구간은 2번 지나게 되므로 결과에 역주행 구간의 거리의 2배를 더한다
            s_point = -1 #시작점을 초기값으로 바꿔준다
    elif start[0]==end[0]: #만약 각 힙의 가장 작은 원소가 같다면 의미 없는 점들이므로
        heapq.heappop(start)
        heapq.heappop(end)# 그 원소들을 제거한다
    elif start[0]<end[0]: #시작점이 끝점보다 작다면 하나의 끝점을 더 만나야 하므로
        heapq.heappop(start) #원소를 제거하고
        count += 1 #카운터를 1 늘린다
print(result)
#----------------------------------------------
#문제 분야 : 힙 정렬
#https://www.acmicpc.net/problem/2836
