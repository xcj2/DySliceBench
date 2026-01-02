#ABC088-D
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return list(input())
h,w=IL()
G=[S() for i in range(h)]
used=[[False for i in range(w)] for j in range(h)]
q=[[0,0,1]]
pos=False
while len(q)>0:
    gy,gx,dis=q.pop(0)
    if gy==h-1 and gx==w-1:
        pos=True
        break
    if not used[gy][gx]:
        if gy!=0:
            if G[gy-1][gx]=="." and not used[gy-1][gx]:
                q.append([gy-1,gx,dis+1])
        if gx!=0:
            if G[gy][gx-1]=="." and not used[gy][gx-1]:
                q.append([gy,gx-1,dis+1])
        if gy!=h-1:
            if G[gy+1][gx]=="." and not used[gy+1][gx]:
                q.append([gy+1,gx,dis+1])
        if gx!=w-1:
            if G[gy][gx+1]=="." and not used[gy][gx+1]:
                q.append([gy,gx+1,dis+1])
    used[gy][gx]=True
if pos:
    ans=0
    for i in range(h):
        ans+=G[i].count(".")
    print(ans-dis)
else:
    print(-1)