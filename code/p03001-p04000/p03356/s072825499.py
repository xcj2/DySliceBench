N,M = map(int,input().split())
p = [i-1 for i in map(int,input().split())]
swap = []
for j in range(M):
    swap.append([i-1 for i in map(int,input().split())])


# 0からn-1まで
n = N

#初期化
par = []
rank = []
for i in range(n):
    par.append(i) # par[i]==iの時root
    rank.append(0) # 深さ
    
def find(x): # rootの探索&縮約
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    elif rank[x]<rank[y]:
        par[x]=y
    else:
        par[y]=x
        if rank[x]==rank[y]:
            rank[x] += 1

for s in swap:
    unite(s[0],s[1])


def same(x,y):
    return find(x)==find(y)

answer = 0
for i in range(N):
    if same(i,p[i]):
        answer += 1
print(answer)
    