import sys
        
def getpar(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[0] = -1
    par[p]  -1
    stack = [p]
    visited = set([p])
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            stack.append(vf)
    return par

def topological_sort_tree(E, r):
    Q = [r]
    L = []
    visited = set([r])
    while Q:
        vn = Q.pop()
        L.append(vn)
        for vf in E[vn]:
            if vf not in visited:
                visited.add(vf)
                Q.append(vf)
    return L

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res


        

N, Q = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

P = getpar(Edge, 0)
L = topological_sort_tree(Edge, 0)
C = getcld(P)

dp1 = [0]*N

for q in range(Q):
    p, x = map(int, sys.stdin.readline().split())
    dp1[p-1] += x

for l in L:
    d = dp1[l]
    for c in C[l]:
        dp1[c] += d

print(' '.join(map(str, dp1))) 
