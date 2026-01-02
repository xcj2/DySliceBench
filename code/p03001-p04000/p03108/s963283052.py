class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [-1 for i in range(n)]

    def root(self, a):
        if self.par[a] < 0:
            return a
        else:
            self.par[a] = self.root(self.par[a])
            return self.par[a]

    def size(self, a):
        return -self.par[self.root(a)]

    def connect(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return False

        if self.size(a) < self.size(b):
            a, b = b, a

        self.par[a] = self.par[a] + self.par[b]
        self.par[b] = a

        return True


def main() -> None:
    N, M = map(int, input().split())
    t = [tuple(map(int, input().split())) for _ in range(M)]
    ans = [0 for _ in range(M)]
    ans[-1] = N * (N - 1) // 2
    uni = UnionFind(N)
    for i in reversed(range(1, M)):
        ans[i - 1] = ans[i]
        a = t[i][0] - 1
        b = t[i][1] - 1
        if uni.root(a) != uni.root(b):
            ans[i - 1] = ans[i - 1] - uni.size(a) * uni.size(b)
            uni.connect(a, b)

    for v in ans:
        print(v)


if __name__ == '__main__':
    main()
