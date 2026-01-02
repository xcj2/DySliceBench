class Graph:
    def __init__(self, n_vertices, edges, directed=True):
        self.n_vertices = n_vertices
        self.edges = edges
        self.directed = directed

    @property
    def adj(self):
        try:
            return self._adj
        except AttributeError:
            adj = [[] for _ in range(self.n_vertices)]
            if self.directed:
                for u,v in self.edges:
                    adj[u].append(v)
            else:
                for u,v in self.edges:
                    adj[u].append(v)
                    adj[v].append(u)
            self._adj = adj
            return adj

class RootedTree(Graph):
    def __init__(self, n_vertices, edges, root_vertex=0):
        self.root = root_vertex
        super().__init__(n_vertices, edges, False)

    @property
    def parent(self):
        try:
            return self._parent
        except AttributeError:
            adj = self.adj
            parent = [None]*self.n_vertices
            parent[self.root] = -1
            stack = [self.root]
            for _ in range(self.n_vertices):
                v = stack.pop()
                for u in adj[v]:
                    if parent[u] is None:
                        parent[u] = v
                        stack.append(u)
            self._parent = parent
            return parent

    @property
    def children(self):
        try:
            return self._children
        except AttributeError:
            children = [None]*self.n_vertices
            for v,(l,p) in enumerate(zip(self.adj,self.parent)):
                children[v] = [u for u in l if u != p]
            self._children = children
            return children

    @property
    def dfs_order(self):
        try:
            return self._dfs_order
        except AttributeError:
            order = [None]*self.n_vertices
            children = self.children
            stack = [self.root]
            for i in range(self.n_vertices):
                v = stack.pop()
                order[i] = v
                for u in children[v]:
                    stack.append(u)
            self._dfs_order = order
            return order

from functools import reduce
from itertools import accumulate,chain
def rerooting(rooted_tree, merge, identity, finalize):
    """
    merge: (T,T) -> T, (T, merge)はモノイド
    identity: 単位元
    finalize: (T, V, V) -> T
 
    以下の形で書けるdpは対応可能
    dp[u,v] = finalize(merge(dp[v,k] for k in adj[v] if k != u), u, v)
    ただし(u,v)は辺
    """
    N = rooted_tree.n_vertices
    parent = rooted_tree.parent
    children = rooted_tree.children
    order = rooted_tree.dfs_order

    # from leaf to parent
    dp_down = [None]*N
    for v in reversed(order):
        dp_down[v] = finalize(reduce(merge,
            (dp_down[c] for c in children[v]),
            identity), parent[v], v)

    # from parent to leaf
    dp_up = [None]*N
    dp_up[0] = identity
    for v in order:
        if len(children[v]) == 0:
            continue
        temp = (dp_up[v],)+tuple(dp_down[u] for u in children[v])+(identity,)
        left = accumulate(temp[:-2],merge)
        right = tuple(accumulate(reversed(temp[2:]),merge))
        for u,l,r in zip(children[v],left,reversed(right)):
            dp_up[u] = finalize(merge(l,r), u, v)

    res = [None]*N
    for v,l in enumerate(children):
        res[v] = reduce(merge,
                    (dp_down[u] for u in children[v]),
                    identity)
        res[v] = merge(res[v], dp_up[v])
    return res,dp_up,dp_down

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

    def merge(x,y):
        cx,nx = x
        cy,ny = y
        c = cx*cy*factorio[nx+ny]*factorio_inv[nx]*factorio_inv[ny]
        return c%MOD, nx+ny

    def finalize(x, u, v):
        c,n = x
        return c,n+1

    t = RootedTree(N,edges)
    res,_,_ = rerooting(t, merge, (1,0), finalize)

    for k,n in res:
        print(k)


import sys
if __name__ == '__main__':
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
     
    N = int(readline())
    m = map(lambda x: int(x)-1, read().split())
    edges = zip(m, m)

    solve(N, edges)
