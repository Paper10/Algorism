#히스토그램의 형태를 반복적으로 입력받는다
arr = []
while True:
    a = list(map(int, input().split(" ")))
    if a[0]==0:
        break
    arr.append(a)

for a in arr: #각 히스토그램 마다 넓이 계산을 실행한다
    his = a[1:] #하스토그램의 개수인 첫번쨰 원소 제거
    stack = [] #히스토그램의 인덱스들을 저장해둘 스택 선언
    i = 0 #히스토그램을 탐색할 인덱스 초기화
    max_square = 0 #결과값을 저장하는 변수
    while i<len(his): #인덱스가 1씩 증가하며 히스토그램을 탐색한다
        if not stack or his[i]>=his[stack[-1]]: #만약 해당 인덱스의 값이 스택에 마지막으로 저장된 값보다 크다면
            stack.append(i) #스택에 해당 인덱스를 넣고
            i += 1 #다음 인덱스로 이동한다
        else: #만약 현재 인덱스의 값이 더 작을경우
            high_index = stack.pop() #스택의 마지막 값을 불러와서
            square = his[high_index] * (i-stack[-1]-1 if stack else i) 
            #해당 인덱스의 값이 시작되었던 인덱스를 구해 (현재 인덱스의 값) * (시작부분 인덱스와 현재 인덱스와의 거리)를 구해
            #해당 사각형의 넓이를 구한다
            max_square = max(max_square, square) #사각형의 최댓값을 업데이트 한다
    while stack: #히스토그램을 모두 돌고 스택에 값이 남아있는 경우 스택이 빌때까지 인덱스의 값이 더 작은 케이스를 반복 실행한다
        high_index = stack.pop()
        square = his[high_index] * (i-stack[-1]-1 if stack else i)
        max_square = max(max_square, square)
    print(max_square) #값 출력

#----------------------------------------------
#문제분야 : 스택
#https://www.acmicpc.net/problem/6549