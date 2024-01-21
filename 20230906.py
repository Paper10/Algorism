import heapq
import sys

n = int(sys.stdin.readline())#정수 n을 입력받는다. sys를 활용한 입력이 더 빠르다고 한다
leftheap = [] # 더 작은 값을 저장할 힙과
rightheap = [] # 더 큰 값을 저장할 힙을 선언한다
for _ in range(n):
    target = int(sys.stdin.readline()) #숫자를 입력받고
    if len(leftheap) == len(rightheap): #만약 두 힙의 크기가 같을경우
        heapq.heappush(leftheap, -target) # 더 작은값을 저장하는 힙에 push한다
                                          # leftheap[0]에 최대값이 나타나게 하기위해 원소에 -1을 곱해 최대힙으로 만든다
    else:
        heapq.heappush(rightheap, target) # 두 힙의 크기가 다를경우 더 큰 값을 저장하는 힙에 push한다 
    if rightheap and rightheap[0]<(leftheap[0]*(-1)): #만약 큰값을 저장하는 힙이 빈 힙이 아니고
                                                      #작은 힙의 최대값이 큰 힙의 최솟값보다 크다면
        left_val = heapq.heappop(leftheap)
        right_val = heapq.heappop(rightheap)#각 힙의 우선순위 0의 원소를 pop하여
        heapq.heappush(leftheap, right_val * (-1))
        heapq.heappush(rightheap, left_val * (-1))#반대로 push 해준다
    print(leftheap[0]*(-1)) # 작은 힙의 우선순위 0 원소를 출력한다. 이때 최대힙을 위해 곱해진 -1을 다시 곱해준다

    #--------------------------------------------------
    #문제 분야 : 우선순위 큐 (힙)
    #https://www.acmicpc.net/problem/1655