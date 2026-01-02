H,W = map(int,input().split())
S = [input() for i in range(H)]

def tor(x,y):
    to = {'6':'3','3':'1','1':'4','4':'6'} if y%4==0 else {'6':'4','4':'1','1':'3','3':'6'}
    return to[S[y][x]]
def tol(x,y):
    to = {'6':'3','3':'1','1':'4','4':'6'} if y%4==2 else {'6':'4','4':'1','1':'3','3':'6'}
    return to[S[y][x]]
def tod(x,y):
    to = {'6':'2','2':'1','1':'5','5':'6'} if x%4==0 else {'6':'5','5':'1','1':'2','2':'6'}
    return to[S[y][x]]
def tou(x,y):
    to = {'6':'2','2':'1','1':'5','5':'6'} if x%4==2 else {'6':'5','5':'1','1':'2','2':'6'}
    return to[S[y][x]]
dxyto = [(0,1,tod),(1,0,tor),(0,-1,tou),(-1,0,tol)]
stack = [(0,0)]
visited = [[0]*W for i in range(H)]
while stack:
    x,y = stack.pop()
    visited[y][x] = 1
    if (x,y) == (W-1,H-1):
        print('YES')
        exit()
    c = S[y][x]
    for dx,dy,to in dxyto:
        nx,ny = x+dx,y+dy
        if not 0 <= nx < W: continue
        if not 0 <= ny < H: continue
        if visited[ny][nx]: continue
        if S[ny][nx] == '#': continue
        if to(x,y) != S[ny][nx]: continue
        stack.append((nx,ny))
print('NO')
