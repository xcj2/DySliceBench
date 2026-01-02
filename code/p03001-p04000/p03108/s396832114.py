import math


class UnionFind:

    def __init__(self, N: int):
        # d[i] = <parent id> if i is a child,
        #       - <size of the group> if i is a root
        self.d = [-1 for _ in range(N)]

    def root(self, x: int) -> int:
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def size(self, x: int):
        return -self.d[self.root(x)]

    def show(self):
        m = {}
        for n in range(len(self.d)):
            r = self.root(n)

            if r not in m:
                m[r] = [n]
            else:
                m[r].append(n)

        print("root -> childs")
        print("---------------------")
        for key in m:
            print("{} -> {}".format(key, m[key]))


class Solution:

    def solve(self, N: int, M: int, bridges):

        # solve
        uf = UnionFind(N+1)

        ans = N * (N-1) // 2
        answer = []

        for a, b in reversed(bridges):
            answer.append(ans)

            if not uf.same(a, b):
                ans -= uf.size(a) * uf.size(b)
                uf.unite(a, b)

        answer.reverse()

        return answer


if __name__ == '__main__':

    # standard input
    N, M = map(int, input().split())
    bridges = []
    for i in range(M):
        bridges.append(tuple(map(int, input().split())))

    # solve
    solution = Solution()
    sol = solution.solve(N, M, bridges)
    for s in sol:
        print(s)
