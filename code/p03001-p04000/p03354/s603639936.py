N,M = [int(s) for s in input().split()]
p = [0] + [int(s) for s in input().split()]
par = []
counter = 0

for i in range(N+1):
    par.append(i)
    
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        par[x] = y

for i in range(M):
    x,y = [int(s) for s in input().split()]
    union(x,y)
    
for i in range(1,N+1):
    if same(i,p[i]):
        counter += 1

print(counter)