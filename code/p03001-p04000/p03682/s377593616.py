import sys
sys.setrecursionlimit(100000)
N=int(input())
xy=[list(map(int,input().split()))+[i] for i in range(N)]
xy.sort()
path = []

def get_par(n):
    if par[n] is None:return n
    par[n] = get_par(par[n])
    return par[n]

def same(i,j):
    return get_par(i) == get_par(j)

def unite(i,j):
    j = get_par(j)
    par[j] = get_par(i)
    return

for k in range(N-1):
    x,y,i = xy[k]
    x2,y2,j = xy[k+1]
    path.append((abs(x-x2),i,j))
xy.sort(key=lambda x:x[1])
for k in range(N-1):
    x,y,i = xy[k]
    x2,y2,j = xy[k+1]
    path.append((abs(y-y2),i,j))
path.sort(key = lambda x:x[0],reverse=True)
par = [None]*N
cnt = 0
ans = 0
while cnt < N-1:
    c,i,j = path.pop()
    if same(i,j):continue
    unite(i,j)
    ans += c
    cnt += 1
print(ans)