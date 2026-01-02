MOD = 10**9 + 7


class modint():
    def __init__(self, value):
        self.value = value % MOD

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return (modint(self.value + other.value) if isinstance(other, modint)
                else modint(self.value + other))

    def __sub__(self, other):
        return (modint(self.value - other.value) if isinstance(other, modint)
                else modint(self.value - other))

    def __mul__(self, other):
        return (modint(self.value * other.value) if isinstance(other, modint)
                else modint(self.value * other))

    def __truediv__(self, other):
        return (modint(self.value * pow(other.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(self.value * pow(other, MOD - 2, MOD)))

    def __pow__(self, other):
        return (modint(pow(self.value, other.value, MOD))
                if isinstance(other, modint)
                else modint(pow(self.value, other, MOD)))

    def __eq__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __ne__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __radd__(self, other):
        return (modint(other.value + self.value) if isinstance(other, modint)
                else modint(other + self.value))

    def __rsub__(self, other):
        return (modint(other.value - self.value) if isinstance(other, modint)
                else modint(other - self.value))

    def __rmul__(self, other):
        return (modint(other.value * self.value) if isinstance(other, modint)
                else modint(other * self.value))

    def __rtruediv__(self, other):
        return (modint(other.value * pow(self.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(other * pow(self.value, MOD - 2, MOD)))

    def __rpow__(self, other):
        return (modint(pow(other.value, self.value, MOD))
                if isinstance(other, modint)
                else modint(pow(other, self.value, MOD)))

    def modinv(self):
        return modint(pow(self.value, MOD - 2, MOD))


def main():
    from heapq import heappush, heappop
    import sys
    readline = sys.stdin.buffer.readline
    N = int(readline())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = (int(i) for i in readline().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    dp = [[modint(1)]*2 for _ in range(N)]
    from collections import deque
    G_color = ['WHITE' for _ in range(N)]
    G_distance = [float('inf') for _ in range(N)]
    G_parent = ['NIL' for _ in range(N)]

    def bfs(G, s):
        leaves = []
        G_color[s] = 'GRAY'
        G_distance[s] = 0
        Q = deque()
        Q.append(s)
        while Q:
            u = Q.popleft()
            has_child = False
            for v in G[u]:
                if G_color[v] == 'WHITE':
                    G_color[v] = 'GRAY'
                    G_distance[v] = G_distance[u] + 1
                    G_parent[v] = u
                    has_child = True
                    Q.append(v)
            G_color[u] = 'BLACK'
            if not(has_child):
                heappush(leaves, (-G_distance[u], u))
        return leaves

    leaves = bfs(edge, 0)
    seen = [False]*N
    while leaves:
        _, leaf = heappop(leaves)
        par = G_parent[leaf]
        if par == 'NIL':
            continue
        dp[par][0] *= dp[leaf][1]
        dp[par][1] *= (dp[leaf][0]+dp[leaf][1])
        if seen[par]:
            continue
        heappush(leaves, (-G_distance[par], par))
        seen[par] = True
    print((dp[0][0]+dp[0][1]))


if __name__ == '__main__':
    main()
