import sys
readline = sys.stdin.readline
popcntsum = ((1<<64) - 1)
Fa = [0] + [popcntsum//((1<<(1<<(i-1)))+1) for i in range(1,7)]
Fb = [0] + [Fa[i]<<(1<<(i-1)) for i in range(1,7)]
fila1 = Fa[1]
filb1 = Fb[1]
fila2 = Fa[2]
filb2 = Fb[2]
fila3 = Fa[3]
filb3 = Fb[3]
fila4 = Fa[4]
filb4 = Fb[4]
fila5 = Fa[5]
filb5 = Fb[5]
fila6 = Fa[6]
filb6 = Fb[6]
def popcount(x):
    x = (x&fila1) + ((x&filb1)>>1)
    x = (x&fila2) + ((x&filb2)>>2)
    x = (x&fila3) + ((x&filb3)>>4)
    x = (x&fila4) + ((x&filb4)>>8)
    x = (x&fila5) + ((x&filb5)>>16)
    x = (x&fila6) + ((x&filb6)>>32)
    return x

def parorder(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[p] = -1
    stack = [p]
    order = []
    Enum = [None]*N
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf, num in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            Enum[vf] = num
            ast(vf)
    return par, order, Enum

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res


N = int(readline())
Edge = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append((b, i))
    Edge[b].append((a, i))

root = 0
P, L, Enum = parorder(Edge, root)
#C = getcld(P)

M = int(readline())
Q = [tuple(map(int, readline().split())) for _ in range(M)]

dp = [0]*(1<<M)
ans = pow(2, N-1)
for S in range(1, 1<<M):
    pc = popcount(S)
    if pc == 1:
        i = (-S&S).bit_length() - 1
        table = [False]*(N-1)
        u, v = Q[i]
        u -= 1
        v -= 1
        while u != root:
            table[Enum[u]] = not table[Enum[u]]
            u = P[u]
        while v != root:
            table[Enum[v]] = not table[Enum[v]]
            v = P[v]
        res = 0
        for t in table:
            res <<= 1
            res |= t
        dp[S] = res
    else:
        dp[S] = dp[S^(-S&S)]|dp[-S&S]
    
    ans += (-1)**(pc%2)*pow(2, N-1-popcount(dp[S]))
print(ans)
