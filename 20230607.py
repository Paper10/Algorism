from collections import deque

#입력부분
n = int(input())
box = []
for _ in range(n):
    arr = list(map(int, input().split(" ")))
    box.append(arr)

#판을 움직이는 함수를 만든다
def move(dir,box):
    b = [[e2 for e2 in e1] for e1 in box]
    
    if dir == "R": #만약 방향이 오른쪽이라면
        for j in range(n): #판을 한줄씩 가져와서
            ar = b[j]
            new = []
            for i in range(n-1,-1,-1):#가져온 배열의 오른쪽부터 탐색한다
                if ar[i]==0:#0이라면 건너뛰고
                    continue
                if not new or not new[0]==ar[i]:#만약 new배열에 아무것도 없거나 가장최근에 new배열에 추가된 수와 다른 수가 입력되면
                    new = [ar[i]] + new#해당 수를 배열 제일 처음에 넣어준다
                elif new[0]==ar[i]:#만약 같은 수가 입력되면
                    new[0] *= (-2)#가장 최근에 new배열에 입력된 수에 -2를 곱해준다
                                  #2가 아닌 -2를 곱하는 이유 : 만약 다음 숫자가 new[0]*2와 같은 수면 중복으로 더해지게 되므로 -2로 이미 합쳐진 수라고 표기
            new = [0] * (n-len(new)) + [abs(e) for e in new]#부족한 원소만큼 배열 앞에 0을 넣어주고 new배열의 원소는 절댓값으로 처리한다
            b[j]=new[:]#만들어진 new배열로 판의 배열을 교체한다

    if dir == "L": #만약 방향이 왼쪽이라면
    #기본적으로 오른쪽일떄와 동일하다.
        for j in range(n):
            ar = b[j]
            new = []
            for i in range(n):#왼쪽의 경우 탐색을 왼쪽부터 시작한다
                if ar[i]==0:
                    continue
                if not new or not new[-1]==ar[i]:
                    new.append(ar[i])
                elif new[-1]==ar[i]:
                    new[-1] *= (-2)
            new = [abs(e) for e in new] + [0] * (n-len(new))#왼쪽의 경우 배열에 오른쪽에 0을 넣는다
            b[j]=new[:]
    
    if dir == "D" or dir == "U":#만약 배열이 위 또는 아래일경우
        #주어진 판의 행과 열을 바꾼후에
        for i in range(n):
            for j in range(n):
                if i>j:
                    b[i][j],b[j][i]=b[j][i],b[i][j]
        #바뀌어진 판을 오른쪽 또는 왼쪽으로 움직이고
        b = move('R',b) if dir=='D' else move('L',b)
        #다시 판의 행과 열을 바꾸면 위 또는 아래로 움직인것과 같은 효과를 낸다
        for i in range(n):
            for j in range(n):
                if i>j:
                    b[i][j],b[j][i]=b[j][i],b[i][j]
    
    return b #움직임이 끝난 판의 형태를 반환한다

result = 0 #가장 큰 수를 저장할 변수
q = deque() #큐를 선언하고
q.append([box,0]) #큐에 처음 주어진 판의 형태와 횟수의 초기값인 0을 넣어준다
while q: #큐에 원소가 없을때까지
    current_box, count = q.popleft()#큐의 원소를 꺼내서
    if count==5:#만약 이미 5회 움직였다면
        for i in range(n):#판을 탐색하면서 result에 가장 큰 수를 저장한다
            for j in range(n):
                result = max(result, current_box[i][j])
    else:#아직 5회 미만이라면 큐에 판을 4방향으로 움직인 결과를 넣어준다
        q.append([move('R',current_box),count+1])
        q.append([move('L',current_box),count+1])
        q.append([move('U',current_box),count+1])
        q.append([move('D',current_box),count+1])

print(result) #결과 출력
#-------------------------------------------------------
#문제 분야 : 브루트 포스
#https://www.acmicpc.net/problem/12100