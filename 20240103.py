
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)

# n!안의 해당 수가 몇개 들어있는지(해당 수의 지수가 몇인지)
def index_check_num(a):
    num = a
    count = 0
    while num <= n:
        count += n // num
        num *= a
    return count


try:
    while True:
        n, k = map(int, input().split())

        # 0!도 1이기 때문에 1로 바꾸어준다.
        if n == 0:
            n = 1

        arr = []  # 소인수 분해한 결과를 담을 변수
        x = k
        for i in range(2, k + 1):
            if i * i > k:
                break
            while x % i == 0:
                arr.append(i)
                x //= i
        if x != 1:
            arr.append(x)

        # 중복을 제거하기 위해 arr을 셋에 담아준다.
        # 2 2 2 3 3 과 같이 들어가있으면 2^3 * 3^2 와같기 때문에
        temp = set(arr)
        result = 1  # 결과를 출력하기 위한 변수

        # n!내에서 각각의 수가 몇개의 지수를 가지고 있는지 체크한 후에
        # 나의 개수와 n!내의 존재개수중 작은 수를 최대 공약수에 곱해준다.
        # 즉, n!내에 2가 6개 곱해져있고 k의 소인수 분해 결과가 2^3 이라면 2^3을 최대공약수에 곱해준다.
        for i in temp:
            if index_check_num(i) != 0:
                num = min(index_check_num(i), arr.count(i))
                result *= (i ** num)
        print(result)

except EOFError:
    exit()


#----------------------------------------------
#문제 분야 : 구현
#https://www.acmicpc.net/problem/7806
