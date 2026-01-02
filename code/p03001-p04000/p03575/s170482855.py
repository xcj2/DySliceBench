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
def func(a):
    return int(a)-1
n,m = map(int,input().split())
par = [-1]*n
ab = [list(map(func,input().split()))for i in range(m)]
ans = 0
for i in range(m):
    par = [-1]*n
    for j in range(m):
        if i != j:
            unite(ab[j][0],ab[j][1])
    for k in range(m):
        if not(same(ab[k][0],ab[k][1])):
            #print(k,ab[k][0]+1,ab[k][1]+1)
            ans += 1
            break

print(ans)