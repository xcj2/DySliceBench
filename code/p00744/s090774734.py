import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


class BipartiteMatching:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pairA = [-1] * N
        self.pairB = [-1] * M
        self.edge = [[] for _ in range(N)]
        self.was = [0] * N
        self.iter = 0

    def add(self, s, t):
        self.edge[s].append(t)

    def _DFS(self, s):
        self.was[s] = self.iter
        for t in self.edge[s]:
            if self.pairB[t] == -1:
                self.pairA[s] = t
                self.pairB[t] = s
                return True
        for t in self.edge[s]:
            if self.was[self.pairB[t]] != self.iter and self._DFS(self.pairB[t]):
                self.pairA[s] = t
                self.pairB[t] = s
                return True
        return False

    def solve(self):
        res = 0
        while True:
            self.iter += 1
            found = 0
            for i in range(self.N):
                if self.pairA[i] == -1 and self._DFS(i):
                    found += 1
            if not found:
                break
            res += found
        return res


def inp(num):
    it = (num + 9) // 10
    res = []
    for _ in range(it):
        res.extend(list(map(int, input().split())))
    return res


if __name__ == "__main__":
    ans = []
    while True:
        M, N = map(int, input().split())
        if M == 0 and N == 0:
            break
        match = BipartiteMatching(M, N)
        Blue = inp(M)
        Red = inp(N)
        for i, b in enumerate(Blue):
            for j, r in enumerate(Red):
                if gcd(b, r) != 1:
                    match.add(i, j)
        ans.append(match.solve())

    print(*ans, sep="\n")

