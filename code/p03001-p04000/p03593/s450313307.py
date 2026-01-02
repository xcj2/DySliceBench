h, w = map(int, input().split())
A = [list(str(input())) for _ in range(h)]

#A = [list('a'*100) for _ in range(h)]

idx = 0
d = {}
C = [0]*26
for i in range(h):
    for j in range(w):
        C[ord(A[i][j])-ord('a')] += 1
        d[(i, j)] = idx
        idx += 1

def Find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = Find(par[x], par)
        return par[x]

def Unite(x, y, par, rank):
    x = Find(x, par)
    y = Find(y, par)

    if x != y:
        if rank[x] < rank[y]:
            par[y] += par[x]
            par[x] = y
        else:
            par[x] += par[y]
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

def Same(x, y, par):
    return Find(x, par) == Find(y, par)

def Size(x, par):
    return -par[Find(x, par)]

n = h*w
par = [-1]*n
rank = [0]*n

for i in range(h):
    for j in range(w):
        p = d[(i, j)]
        q = d[(i, w-1-j)]
        Unite(p, q, par, rank)
        q = d[(h-1-i, j)]
        Unite(p, q, par, rank)

S = []
for i in range(n):
    if par[i] < 0:
        S.append(-par[i])
S.sort(reverse=True)
#print(S)
#print(len(S))
#print(C)

C = [-c for c in C]
import heapq
heapq.heapify(C)
for s in S:
    c = -heapq.heappop(C)
    if c >= s:
        c -= s
        heapq.heappush(C, -c)
    else:
        print('No')
        exit()
else:
    print('Yes')
