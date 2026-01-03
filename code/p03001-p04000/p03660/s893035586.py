N = int(input())
ab = [list(map(int,input().split())) for i in range(N-1)]

adj = [[]for i in range(N+1)]
for i in range(N-1):
    a,b = ab[i]
    adj[a].append(b)
    adj[b].append(a)


from collections import deque 
#スタック
s = deque([])

cost = [10**10]*(N+1)

s.append([1,0])
while len(s)>0:
    place,time = s.pop()
    if time > cost[place]:
        continue
    cost[place]=time
    for i in adj[place]:
        if time < cost[i]:
            s.append([i,time+1])

#たどる
root = [N]
nowp = N
nowt = cost[N]
while nowt>0:
    for i in adj[nowp]:
        if cost[i]==nowt-1:
            root.append(i)
            nowp=i
            nowt=nowt-1
            break

feneaba = len(root)//2-1
l,r = min(root[feneaba],root[feneaba+1]),max(root[feneaba],root[feneaba+1])

#Union Find
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

#初期化
#根なら-size,子なら親の頂点
par = [-1]*(N+1)

for i in range(N-1):
    a,b = ab[i]
    a,b = min(a,b),max(a,b)
    if a==l and b==r:
        continue
    unite(a,b)

print("Fennec" if size(1)>size(N) else "Snuke")