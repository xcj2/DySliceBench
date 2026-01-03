import sys

#UnionFine　ネットの解答

def find(x,par):
    if par[x] == x:
        return x
    else:
        return find(par[x],par)

def union(x,y,par,rank):
    x = find(x,par)
    y = find(y,par)

    if x != y:
        #xとyの属している集合が異なる場合
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

def same(x,y,par):
    return find(x,par) == find(y,par)

input = sys.stdin.readline
n, k, l = map(int, input().split())    
apar = []
bpar = []
arank = [0]*n
brank = [0]*n

for i in range(n):
    apar.append(i)
    bpar.append(i)


for i in range(k):
    p,q = map(int, input().split())
    union(p-1,q-1,apar,arank)

for i in range(l):
    p,q = map(int, input().split())
    union(p-1,q-1,bpar,brank)

num = []
d = {}
for i in range(n):
    num.append(find(i,apar)+find(i,bpar)*10**6)
    if num[-1] in d:
        d[num[-1]] += 1
    else:
        d[num[-1]] = 1

res = ''
for i in range(n):
    if i != 0:
        res += ' '

    res += str(d[num[i]])

print(res)