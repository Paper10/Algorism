n = int(input())
shape = [[1,1,1],[1,0,1],[1,1,1]] #기본 형태를 선언한다

def bigger(base): # 입력된 형태를 정해진 규칙대호 3x3 크기로 늘려주는 함수
  big = len(base)*3 # 반환할 형태의 크기를 선언하고
  tar = [[0 for i in range(big)] for j in range(big)] #전부 0으로 채워 초기화 한다
  for i in range(3):
    for j in range(3):
      if i==1 and j==1: # 가운데 부분은 규칙에 따라 비운다
        continue
      start_i = i * len(base)
      start_j = j * len(base)#커진 형태의 가장 첫번째 인덱스를 기준으로 복사를 시작한다
      for a in range(len(base)):
        for b in range(len(base)):
          tar[a+start_i][b+start_j] = base[a][b]
  return tar

while(True):
  if len(shape)>=n:
    break
  else:
    shape=bigger(shape) #입력된 숫자에 따라 반복한다

for i in range(n):
  for j in range(n):
    if shape[i][j]==1:
      print('*', end='')
    else:
      print(' ', end='')
  print('') #출력부분
#----------------------------------------------------------
#문제 분야 : 재귀
#https://www.acmicpc.net/problem/2447