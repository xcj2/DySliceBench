import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

mod = 10**9+7

n = int(input())
g = [[] for _ in range(n)]

pow2 = [0 for _ in range(n+1)]
pow2[0] = 1
for i in range(n):
    pow2[i+1] = pow2[i]*2 % mod

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


def func(x):
    return pow2[x]-1


class Tree:
    def __init__(self, crdinal, adjgrph, root, fnction=lambda x: 0):
        self.crdinal = crdinal
        self.adjgrph = adjgrph
        self.root = root
        self.fnction = fnction
        self.parent = [-1]*self.crdinal
        self.depth = [-1]*self.crdinal
        self.subsize = [1]*self.crdinal
        self.result = [0]*self.crdinal

        s = [root]
        while s:
            v = s.pop()
            if self.depth[v] == -1:
                if v == root:
                    self.depth[v] = 0
                else:
                    self.depth[v] = self.depth[self.parent[v]] + 1
                    s.append(v)
                for w in self.adjgrph[v]:
                    if self.depth[w] == -1:
                        self.parent[w] = v
                        s.append(w)
            else:
                self.subsize[self.parent[v]] += self.subsize[v]
                self.result[self.parent[v]] += self.fnction(self.subsize[v])

    def parent(self) -> list:
        return self.parent

    def depth(self) -> list:
        return self.depth

    def size(self) -> list:
        return self.subsize

    def result(self) -> list:
        return self.result


tr = Tree(n, g, 0, func)
sizesub = tr.subsize
black = tr.result


cnt = 0

for i in range(n):
    tmp = pow2[n-1] - pow2[n-sizesub[i]] - black[i]
    tmp %= mod
    cnt += tmp
    cnt %= mod


def inv(a, mod):
    r = [1, 0, a]
    w = [0, 1, mod]
    while w[2] != 1:
        q = r[2]//w[2]
        r_new = [r[0]-q*w[0], r[1]-q*w[1], r[2]-q*w[2]]
        r = w
        w = r_new
    x, y = w[0], w[1]    # a*x+y*mod = 1
    return (mod+x % mod) % mod


print(inv(pow2[n], mod)*cnt % mod)
