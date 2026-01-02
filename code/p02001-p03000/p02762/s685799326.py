import sys
input = sys.stdin.readline

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True
    
def same(x,y):
    return find(x) == find(y)

def size(x):
    return -par[find(x)]

n,m,k = map(int,input().split())
ab = [list(map(int,input().split()))for i in range(m)]
cd = [list(map(int,input().split()))for i in range(k)]

friend = [0]*(n+1)
for i in range(m):
    friend[ab[i][1]] += 1
    friend[ab[i][0]] += 1

par = [-1]*(n+1)
for i in range(m):
    unite(ab[i][0],ab[i][1])

block = [0]*(n+1)
for i in range(k):
    if same(cd[i][0],cd[i][1]):
        block[cd[i][0]] += 1
        block[cd[i][1]] += 1
    #block[cd[i][0]].append(cd[i][1])
    #block[cd[i][1]].append(cd[i][0])



for i in range(1,n+1):
    print(size(i)-friend[i]-block[i]-1,end = " ")
