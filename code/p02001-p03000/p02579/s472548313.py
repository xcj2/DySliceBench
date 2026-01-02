#01BFS

H,W = map(int,input().split())
CH,CW = map(int,input().split())
DH,DW = map(int,input().split())
S=[None]*H
for i in range(H):
    S[i] = input()

from collections import deque
def in_area(x,y):
    return 0<=x<=H-1 and 0<=y<=W-1
    
def cango_step(x,y):
    cand0 =[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    cand=[c for c in cand0 if in_area(*c)]
    return cand

def cango_warponly(x,y):
    cand0 =[(x-2,y-2),(x-2,y-1),(x-2,y),(x-2,y+1),(x-2,y+2),
            (x+2,y-2),(x+2,y-1),(x+2,y),(x+2,y+1),(x+2,y+2),
            (x+1,y-2),(x,y-2),(x-1,y-2),
            (x+1,y+2),(x,y+2),(x-1,y+2),
            (x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
    cand=[c for c in cand0 if in_area(*c)]
    return cand

q = deque([(-1,-1,CH-1,CW-1,0)]) 
been = [[False]*W for _ in range(H)]
INF=10**20
shortest =[[INF]*W for _ in range(H)]
shortest[CH-1][CW-1] = 0
    
reach=False
while q:
    x_old,y_old,x_now,y_now,time = q.pop()
    #print(x_now,y_now,time)
    
#     if x_now==H-1 and y_now==W-1:
#         reach=True
#         break
        
    cand = cango_step(x_now,y_now)
    for x_new,y_new in cand:
        if S[x_new][y_new]=="." and shortest[x_new][y_new]>time:
            q.append((x_now,y_now,x_new,y_new,time))
            shortest[x_new][y_new]=time
            
    cand = cango_warponly(x_now,y_now)
    for x_new,y_new in cand:
        if S[x_new][y_new]=="." and shortest[x_new][y_new]>time+1:
            q.appendleft((x_now,y_now,x_new,y_new,time+1))
            shortest[x_new][y_new]=time+1
            
if shortest[DH-1][DW-1]==INF:
    print(-1)
else:
    print(shortest[DH-1][DW-1])       
