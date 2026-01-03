import sys
readline = sys.stdin.readline
from collections import Counter 

def calc(A):
    s = sum(A)
    ma = max(A)
    if 2*ma > s:
        return s - ma
    return s//2

def check():
    candi = [[] for _ in range(N)]
    for l in L[:0:-1]:
        p = P[l]
        if candi[l]:
            x = sum(candi[l]) - A[l]
            y = A[l] - x
            if not 0 <= x <= calc(candi[l]):
                return 'NO'
        else:
            x = 0
            y = A[l]
        candi[p].append(y)
    x = sum(candi[root]) - A[root]
    y = A[root] - x
    if candi[root]:
        if not 0 <= x <= calc(candi[root]):
            return 'NO'
    if y:
        return 'NO'         
    return 'YES'

def parorder(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return par, order

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res


N = int(readline())
A = list(map(int, readline().split()))
Edge = [[] for _ in range(N)]
Dim = [0]*N
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
    Dim[a] += 1
    Dim[b] += 1

if N == 2:
    ans = 'YES' if A[0] == A[1] else 'NO'
else:
    root = Dim.index(max(Dim))
    P, L = parorder(Edge, root)
    C = getcld(P)
    ans = check()

print(ans)
