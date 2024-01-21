
import heapq
import sys
from collections import deque
input = sys.stdin.readline


def solution(food_times, k):
    # 음식의 총 개수
    n = len(food_times)

    # 음식을 섭취하는데 걸리는 시간의 합
    total_time = sum(food_times)

    # 음식을 모두 먹는데 걸리는 시간이 k보다 작으면 -1 반환
    if total_time <= k:
        return -1

    # 음식의 시간과 인덱스를 튜플로 묶은 리스트 생성
    foods = [(time, idx) for idx, time in enumerate(food_times)]

    # 음식 시간을 기준으로 오름차순 정렬
    foods.sort()

    # 이전에 먹은 음식 시간
    prev_time = 0

    # 음식의 인덱스를 순회하면서 남은 시간과 비교
    for i, (time, idx) in enumerate(foods):
        # 이전에 먹은 음식 시간을 빼서 걸린 시간 계산
        diff = time - prev_time

        # 현재 음식을 다 먹는데 걸리는 시간
        curr_time = diff * (n - i)

        # k보다 현재 음식을 다 먹는데 걸리는 시간이 작거나 같으면
        if curr_time <= k:
            # k에서 현재 음식을 다 먹는데 걸리는 시간을 뺌
            k -= curr_time
            # 이전에 먹은 음식 시간 갱신
            prev_time = time
        else:
            # k보다 현재 음식을 다 먹는데 걸리는 시간이 크면
            # 남은 음식들 중에서 남은 시간에 해당하는 음식을 찾아 반환
            remaining_foods = sorted(foods[i:], key=lambda x: x[1])
            return remaining_foods[k % len(remaining_foods)][1] + 1


#----------------------------------------------
#문제 분야 : 구현
#https://school.programmers.co.kr/learn/courses/30/lessons/42891
