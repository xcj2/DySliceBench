n,m = map(int,input().split())
pairs = []
for i in range(m):
    a,b = map(int,input().split())
    pairs.append([a-1,b-1])

ans = [0]*m
P = [-1]*n

def find(a):
    if(P[a] < 0):
        return a
    P[a] = find(P[a])
    return P[a]

def same(a, b):
    return find(a) == find(b)

def size(a):
    return -P[find(a)]

def unite(a,b):
    a = find(a)
    b = find(b)
    if(a == b):
        return false
    if(P[a] > P[b]):
        a,b = b,a
    P[a] += P[b]
    P[b] = a

t = n*(n-1)/2

for i in range(m):
    ans[m-1-i] = int(t)
    u,v = pairs[m-1-i][0],pairs[m-1-i][1]
    if(same(u,v)):
        continue
    else:
        t-= size(u)*size(v)
        unite(u,v)

print(*ans,sep = "\n")
