def find_root(root,x):
    y = root[x]
    if x == y:
        return x
    z = find_root(root,y)
    root[x] = z
    return z
 
def merge(root,size,x,y):
    x = find_root(root,x)
    y = find_root(root,y)
    if x == y:
        return
    sx,sy = size[x],size[y]
    if sx < sy:
        sx,sy = sy,sx
        x,y = y,x
    root[y] = x
    size[x] += sy
    
def UF_check(root,x,y):
    if find_root(root,x) == find_root(root,y):
        return True
    else:
        return False
    
def UF_make(graph,n):  #グラフと最大項を与えると、塊ごとにグルーピングする
    Root=list(range(n+1))
    Size=[1] * (n+1)
    for i in range(len(graph)):
        merge(Root,Size,graph[i][0],graph[i][1])
    for i in range(n+1):  #これを入れれば、UF_checkを使わずに一塊になる
        Root[i] = find_root(Root,i)
    Root.pop(0)  #
    return Root

N,M=map(int,input().split())
P=list(map(int,input().split()))
XY=[list(map(int,input().split())) for i in range(M)]

UF=UF_make(XY,N)
#print(UF)

groups=[[] for i in range(N+1)]
for i in range(N):
    groups[UF[i]].append(P[i])

for i in range(N+1):
    groups[i].sort()

import bisect
ans=0
for i in range(N):
    num=bisect.bisect_left(groups[UF[i]],i+1)
    if num!=len(groups[UF[i]]) and groups[UF[i]][num]==i+1:
        ans+=1

print(ans)