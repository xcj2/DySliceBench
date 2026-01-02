N, M = map(int,input().split())
V = [[int(i)-1 for i in input().split()] for j in range(M)]
ans = [0]*M
P = [-1]*N

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
    
t = N*(N-1)//2
for i in range(M):
    ans[M-1-i] = t
    u,v = V[M-1-i]
    if(same(u,v)):
        continue
    else:
        t -= size(u)*size(v)
        unite(u,v)

print(*ans,sep="\n")
    
