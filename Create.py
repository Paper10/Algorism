import os
import datetime
# 파이썬 파일 생성 코드

# 파일에 들어갈 내용
content = """
import heapq
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
sys.setrecursionlimit(10000)



#----------------------------------------------
# : 
#
"""

# 현재 디렉토리 경로
dir_path = os.path.dirname(os.path.realpath(__file__))

# 오늘 날짜
today = datetime.date.today()

# 파일명 생성
next_file_name = today.strftime("%Y%m%d") + ".py"
next_file_path = os.path.join(dir_path, next_file_name)

# 새 파일 생성 및 내용 추가
with open(next_file_path, "w") as file:
    file.write(content)

print(f"새로운 파일 '{next_file_name}'가 생성되었습니다.")
