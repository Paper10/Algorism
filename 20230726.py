import heapq
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def team(now):
    global result
    visit[now]=True#현재 노드를 방문처리하고
    if visit[arr[now]]:#만약 해당 노드가 이미 방문한 노드이고
        if arr[now] in cycle:#현재 사이클에 해당 노드가 포함되어 있다면
            result+=len(cycle)-cycle.index(arr[now])#해당 노드부터 시작하는 사이클의 길이를 결과에 더한다
    else:
        cycle.append(arr[now]) #아니라면 사이클에 해당 노드를 추가하고
        team(arr[now])#재귀적으로 다음 노드에 대한 함수를 호출한다
        

result = 0
N = int(input())
for _ in range(N):
    length = int(input())
    arr = [0] + list(map(int,input().split()))
    visit = [False]*(length+1) #방문 처리를 위한 학생 수와 같은 길이의 배열 생성

    for i in range(1,length+1):
        if visit[i] : continue #만약 이미 방문한 노드라면 넘어간다
        else:#방문하지 않은 노드에 대해
            cycle = [i] #초기값을 넣어주고
            team(i)#함수를 호출한다

    print(length-result) #그룹이 없는 학생 수 이므로 전체 학생에서 결과값을 뺀다
    result=0
#----------------------------------------------
#문제 분야 : BFS
#https://www.acmicpc.net/problem/9466
