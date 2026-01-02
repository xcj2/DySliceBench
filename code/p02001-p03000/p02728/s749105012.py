
import sys
from functools import reduce
def rerooting(N, adj, merge, finalize,identity):
    """
    merge: (T,T) -> T
    This merges two dp results. (T, operator) must be a monoid.

    identity: identity of (T, operator)
    
    finalize: T -> T
    This transforms the merged result to the dp result
    """

    order = [None]*N
    parent = [None]*N
    parent[0] = -1
    stack = [0]
    for i in range(N):
        v = stack.pop()
        order[i] = v
        for u in adj[v]:
            if parent[u] is None:
                parent[u] = v
                stack.append(u)

    # from leaf to parent
    dp_down = [None]*N
    for v in reversed(order[1:]):
        p = parent[v]
        dp_down[v] = finalize(reduce(merge,
            (dp_down[c] for c in adj[v] if c != p),
            identity))

    # from parent to leaf
    dp_up = [None]*N
    dp_up[0] = identity
    for v in order:
        if len(adj[v]) == 1 and adj[v][0] == parent[v]:
            continue
        p = parent[v]
        left = [dp_up[v]]
        for u in adj[v]:
            if u != p:
                left.append(merge(left[-1],dp_down[u]))

        right = [identity]
        for u in reversed(adj[v]):
            if u != p:
                right.append(merge(dp_down[u],right[-1]))
        i = 0
        for u in adj[v]:
            if u != p:
                dp_up[u] = finalize(merge(left[i],right[-i-2]))
                i += 1

    for v,l in enumerate(adj):
        order[v] = reduce(merge,
                    (dp_down[u] for u in adj[v] if u != parent[v]),
                    identity)
        order[v] = finalize(merge(order[v], dp_up[v]))

    return order


def solve(N,edges):
    MOD = 10**9+7

    factorio = [None]*(N+1)
    factorio[0] = 1
    t = 1
    for i in range(1,N+1):
        t *= i
        t %= MOD
        factorio[i] = t

    factorio_inv = [None]*(N+1)
    factorio_inv[0] = 1
    t = pow(factorio[-1],MOD-2,MOD)
    for i in reversed(range(1,N+1)):
        factorio_inv[i] = t
        t *= i
        t %= MOD


    adj = [[] for _ in range(N)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def func(x,y):
        cx,nx = x
        cy,ny = y
        c = cx*cy*factorio[nx+ny]*factorio_inv[nx]*factorio_inv[ny]
        return c%MOD, nx+ny

    def func2(x):
        c,n = x
        return c,n+1

    identity = (1,0)

    res = rerooting(N, adj, func, func2, identity)

    for k,n in res:
        print(k)


if __name__ == '__main__':
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
     
    N = int(readline())
    m = map(int, read().split())
    edges = tuple((a-1,b-1) for a,b in zip(m, m))

    solve(N, edges)
