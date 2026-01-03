import sys

def find(x,par,rank):
    if par[x] == x : return x
    else:
        par[x] = find(par[x],par,rank)
        return par[x]

def unite(x,y,par,rank): 
    x = find(x,par,rank)
    y = find(y,par,rank)
    if (x != y):
        if rank[x] < rank[y]:
            par[x] = y
        else :
            par[y] = x
            if (rank[x] == rank[y]) : rank[x] += 1

def same(x,y,par,rank):
    return (find(x,par,rank) == find(y,par,rank)) 

n,k,l = map(int, sys.stdin.readline().split())

par1 = [i for i in range(n)]
par2 = [i for i in range(n)]
rank1 = [0 for i in range(n)]
rank2 = [0 for i in range(n)]

for i in range(k):
    pp,qq = map(int, sys.stdin.readline().split())
    unite(pp-1,qq-1,par1,rank1)

for i in range(l):
    rr,ss = map(int, sys.stdin.readline().split())
    unite(rr-1,ss-1,par2,rank2)

dic = {}
parlis = []
for i in range(n):
    p1 = find(i,par1,rank1)
    p2 = find(i,par2,rank2)
    parlis.append((p1,p2))
    if (p1,p2) in dic:
        dic[(p1,p2)] += 1
    else: 
        dic[(p1,p2)] = 1

ans =[]

for i in range(n):
    ans.append(dic[parlis[i]])

print(*ans)