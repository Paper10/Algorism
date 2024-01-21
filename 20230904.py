from collections import deque

n,m = map(int, input().split(" "))
map = []
for i in range(n):
    arr = [char for char in list(input())]
    map.append(arr)

def move(dir,map_origin):
    rx,ry,bx,by = 0,0,0,0
    map=[[e2 for e2 in e1] for e1 in map_origin]
    for i in range(n):
        for j in range(m):
            if map[i][j]=='R':
                rx = j
                ry = i
            if map[i][j]=='B':
                bx = j
                by = i
    d = {'R':[1,0],'L':[-1,0],'U':[0,-1],'D':[0,1]}
    if not map[ry+d[dir][1]][rx+d[dir][0]]=='.' and not map[by+d[dir][1]][bx+d[dir][0]]=='.':
        return [-2,[[]]]
    for _ in range(2):
        while map[ry+d[dir][1]][rx+d[dir][0]]=='.':
            map[ry][rx]='.'
            map[ry+d[dir][1]][rx+d[dir][0]]='R'
            rx=rx+d[dir][0]
            ry=ry+d[dir][1]
        while map[by+d[dir][1]][bx+d[dir][0]]=='.':
            map[by][bx]='.'
            map[by+d[dir][1]][bx+d[dir][0]]='B'
            bx=bx+d[dir][0]
            by=by+d[dir][1]
        if map[by+d[dir][1]][bx+d[dir][0]]=='O':
            return [-1,map]
    if map[ry+d[dir][1]][rx+d[dir][0]]=='O':
        if map[by+d[dir][1]*2 if 0<=by+d[dir][1]*2<n else by][bx+d[dir][0]*2 if 0<=bx+d[dir][0]*2<m else bx]=='O':
            return [-1,map]
        else:
            return [1,map]
    return [0,map]


q=deque()
q.append(['X',0,[[e2 for e2 in e1] for e1 in map]])
direction = ['R','L','U','D']
while q:
    dir,count,current_map = q.popleft()
    if count >= 10:
        continue
    for d in direction:
        if not d == dir:
            result,next_map = move(d,current_map)
            if result == 1:
                print(count+1)
                exit()
            elif result == -1:
                continue
            elif result == -2:
                continue
            else:
                q.append([d,count+1,[[e2 for e2 in e1] for e1 in next_map]])
if not q:
    print(-1)
