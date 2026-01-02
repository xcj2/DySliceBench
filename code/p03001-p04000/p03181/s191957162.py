
from functools import reduce
from itertools import accumulate,chain
def rerooting(N, adj, merge, identity, finalize):
    """
    merge: (T,T) -> T, (T, merge)はモノイド
    identity: 単位元
    finalize: T -> T

    以下の形で書けるdpは対応可能
    dp[u,v] = finalize(merge(dp[v,k] for k in adj[v] if k != u))
    ただし(u,v)は辺
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
        p = parent[v]
        if len(adj[v]) == 1 and adj[v][0] == p:
            continue
        left = tuple(accumulate(
            chain((dp_up[v],),(dp_down[u] for u in adj[v] if u != p)),
            merge))
        right = tuple(accumulate(
            chain((identity,),(dp_down[u] for u in reversed(adj[v]) if u != p)),
            merge))
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

def solve(N,M,E):

    adj = [[] for _ in range(N)]
    for a,b in E:
        adj[a].append(b)
        adj[b].append(a)

    def merge(x,y):
        return (x*y)%M
    def finalize(x):
        return x+1

    res = rerooting(N,adj,merge,1,finalize)
    return [v-1 for v in res]


if __name__ == '__main__':
    N,M = map(int,input().split())
    E = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(N-1)]
    print(*solve(N,M,E),sep='\n')