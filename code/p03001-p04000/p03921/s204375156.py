import sys
sys.setrecursionlimit(2 * 10**5)
N,M = map(int,input().split())

par = [i for i in range(N+M)]
def root(a):
    if par[a] == a: return a
    par[a] = root(par[a])
    return par[a]

def same(a,b):
    return root(a) == root(b)

def unite(a,b):
   ra,rb = root(a),root(b)
   if ra == rb: return
   par[ra] = rb

for i in range(N):
    src = list(map(lambda x:int(x)-1,input().split()))
    if len(src) == 1: continue
    for j in src[1:]:
        unite(i,N+j)

for i in range(1,N):
    if not same(0,i):
        print('NO')
        exit()
print('YES')