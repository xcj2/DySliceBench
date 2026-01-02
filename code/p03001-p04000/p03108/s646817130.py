# お約束
INF = float("inf")
MOD = int(1e9 + 7)
def int1(n):
    return int(n) - 1
def parse(*args):
    # (tuple(map(int, input().split())) for _ in range(N))
    return tuple(p(v) for p, v in zip(args, input().split()))

# Union-Find木
class uft:
    def __init__(self, n):
        self.height = [1] * n
        self.group = [-1] * n
    def root(self, v):
        if self.group[v] < 0:
            return v
        self.group[v] = self.root(self.group[v])
        return self.group[v]
    def size(self, v):
        return - self.group[self.root(v)]
    def equal(self, v1, v2):
        v1, v2 = self.root(v1), self.root(v2)
        return v1 == v2
    def merge(self, v1, v2):
        v1, v2 = self.root(v1), self.root(v2)
        if self.equal(v1, v2):
            return False
        if self.height[v1] < self.height[v2]:
            self.group[v2] += self.group[v1]
            self.group[v1] = v2
            self.height[v2] = max(self.height[v1] + 1, self.height[v2])
        else:
            self.group[v1] += self.group[v2]
            self.group[v2] = v1
            self.height[v1] = max(self.height[v1], self.height[v2] + 1)
        return True

# エントリーポイント
def main():
    N, M = parse(int, int)
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    fuben = N * (N - 1) // 2
    g, rs = uft(N), [fuben]
    for a, b in reversed(AB):
        a, b = a - 1, b - 1
        if not g.equal(a, b):
            fuben -= g.size(a) * g.size(b)
            g.merge(a, b)
        rs += [fuben]
    for r in reversed(rs[:-1]):
        print(r)

main()
