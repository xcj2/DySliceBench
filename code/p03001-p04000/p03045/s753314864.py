def init(n):
    for i in range(N):
        par[i] = i
        rnk[i] = 0

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if (rnk[x] < rnk[y]):
        par[x] = y
    else:
        par[y] = x
        if(rnk[x] == rnk[y]):
            rnk[x] += 1
            
N, M = map(int, input().split())

X = [0 for i in range(M)]
Y = [0 for i in range(M)]
Z = [0 for i in range(M)]

for i in range(M):
    X[i], Y[i], Z[i] = map(int, input().split())
    X[i] -= 1
    Y[i] -= 1

par = [0 for i in range(N)]
rnk = [0 for i in range(N)]
init(N)

for i in range(M):
    unite(X[i], Y[i])
    
for i in range(N):
  find(i)

print(len(set(par)))