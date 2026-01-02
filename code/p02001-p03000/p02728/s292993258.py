import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


class Tree:
    def __init__(self, crdinal, adjgrph, root):
        self.n = crdinal
        self.g = adjgrph
        self.root = root
        self.parent = [-1]*self.n
        self.depth = [-1]*self.n
        self.subsize = [1]*self.n
        self.dp = [1]*self.n  # 0 : additive, 1 : multiplicative

        s = [self.root]
        while s:
            v = s.pop()
            if self.depth[v] == -1:
                if v == self.root:
                    self.depth[v] = 0
                else:
                    self.depth[v] = self.depth[self.parent[v]] + 1
                    s.append(v)
                for w in self.g[v]:
                    if self.depth[w] == -1:
                        self.parent[w] = v
                        s.append(w)
            else:
                self.subsize[self.parent[v]] += self.subsize[v]
                self.calc(v)

        for i in range(n):
            self.dp[i] *= fact[self.subsize[i]-1]
            self.dp[i] %= mod

    def calc(self, v):
        # The following formula is calculated by bottom-up:
        self.dp[self.parent[v]] *= fact[self.subsize[v]-1] * self.dp[v] * ifact[self.subsize[v]]
        self.dp[self.parent[v]] %= mod
        return None

    def wanted(self):
        # Edit the item you want by using self.depth, self.subsize, etc..
        # Default : self.parent
        return self.parent

    def rerooting(self) -> list:
        # Modify below if you want to use rerooting
        ans = [0]*n
        ans[self.root] = self.dp[self.root]

        FromParent = [0]*n

        s = [self.root]
        while s:
            v = s.pop()
            cum = 1

            for w in self.g[v]:
                if w != self.parent[v]:
                    cum *= self.dp[w]*ifact[self.subsize[w]]
                    cum %= mod
                    s.append(w)
                else:
                    cum *= FromParent[v]*ifact[n-self.subsize[v]]
                    cum %= mod

            # calculate the sub-result for parent's subtree when you see the child as root.
            # get the answer for each child.
            for i, w in enumerate(self.g[v]):
                if w != self.parent[v]:
                    FromParent[w] = fact[n-self.subsize[w]-1] * cum * inv(self.dp[w] * ifact[self.subsize[w]] , mod)
                    ans[w] = fact[n-1] * (FromParent[w] * ifact[n-self.subsize[w]]) * (self.dp[w] * ifact[self.subsize[w]-1])
                    ans[w] %= mod
        return ans


mod = 10**9+7


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


max_num = 2*10**5+1
fact = [0 for _ in range(max_num)]
ifact = [0 for _ in range(max_num)]

fact[0] = fact[1] = 1
ifact[0] = ifact[1] = 1

for i in range(2, max_num):
    fact[i] = fact[i-1] * i % mod

ifact[max_num-1] = inv(fact[max_num-1], mod)

for i in range(2, max_num):
    ifact[max_num-i] = (ifact[max_num-i+1] * (max_num-i+1)) % mod


n = int(input())
g = [[] for _ in range(n)]

for _ in range(n-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

T1 = Tree(n, g, 0)

for x in T1.rerooting():
    print(x)
