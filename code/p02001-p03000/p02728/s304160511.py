import sys
readline = sys.stdin.readline


def treedoubling(P):
    #根の親は-1
    P = P[:]
    N = len(P)
    D = [P[:]]
    dep = N.bit_length()
    for _ in range(dep):
        ret = [-1]*N
        for i in range(N):
            k = D[-1][i]
            if k != -1:
                ret[i] = D[-1][k]
        D.append(ret)
    return D

def lca(u, v, D, par, dist):
    if dist[u] > dist[v]:
        u, v = v, u
    
    ddif = dist[v] - dist[u]
    for i in range(ddif.bit_length()):
        if (1<<i)&ddif:
            v = D[i][v]
    
    if u != v:
        for cnt in range(dist[u].bit_length()-1, -1, -1):
            if D[cnt][u] != D[cnt][v]:
                u = D[cnt][u]
                v = D[cnt][v]
        u = par[u]
    return u

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

def rerootingdp(P, L, intv = None):
    def merge(x, y):
        if x == intv:
            return y
        if y == intv:
            return x
        sa, da = x
        sb, db = y
        return (sa + sb, da*db%MOD)

    def g(m, vn):
        if m == intv:
            return (1, 1)
        sc, dc = m
        return (sc+1, dc*frac[sc]*fraci[sc+1]%MOD)
    
    N = len(L)
    dp = [None]*N
    LR = [intv]*N
    D = [intv]*N
    cld = [[] for _ in range(N)]
    for l in L[::-1]:        
        resl = intv
        for ci in cld[l]:
            LR[ci] = merge(LR[ci], resl)
            resl = merge(resl, dp[ci])
        resr = intv
        for ci in cld[l][::-1]:
            LR[ci] = merge(LR[ci], resr)
            resr = merge(resr, dp[ci])
        D[l] = resr
        dp[l] = g(resr, l)
        
        if P[l] != -1:
            cld[P[l]].append(l)
        
    U = [None]*N
    ans = [None]*N
    U[L[0]] = intv
    ans[L[0]] = dp[L[0]]
    for l in L[1:]:
        p = P[l]
        U[l] = g(merge(U[p], LR[l]), p)
        ans[l] = g(merge(D[l], U[l]), l)    
    return ans 

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p):
        if v == -1:
            continue
        res[v].append(i)
    return res


MOD = 10**9+7
def frac(limit):
    frac = [1]*limit
    for i in range(2,limit):
        frac[i] = i * frac[i-1]%MOD
    fraci = [None]*limit
    fraci[-1] = pow(frac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
        fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
    return frac, fraci
frac, fraci = frac(1341398)

N = int(readline())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)



P, L = parorder(Edge, 0)

Ans = [frac[a]*d%MOD for a, d in rerootingdp(P, L)]
print('\n'.join(map(str, Ans)))
