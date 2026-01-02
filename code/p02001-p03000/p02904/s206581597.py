import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    from collections import deque
    N, K = map(int, readline().split())
    P = list(map(int, readline().split()))

    if N == K:
        return print(1)

    p_min = [0] * (N - K)
    p_max = [0] * (N - K)
    p_asc = [0] * (N - K + 1)

    def calc_min():
        que = deque()
        que.append(P[0])

        for i in range(1, K + 1):
            cur = P[i]
            while que and cur < que[-1]:
                que.pop()
            que.append(cur)
        p_min[0] = que[0]

        for i in range(N - K - 1):
            prev = P[i]
            cur = P[i + K + 1]
            if que[0] == prev:
                que.popleft()
            while que and cur < que[-1]:
                que.pop()
            que.append(cur)
            p_min[i + 1] = que[0]

    def calc_max():
        que = deque()
        que.append(P[0])

        for i in range(1, K + 1):
            cur = P[i]
            while que and cur > que[-1]:
                que.pop()
            que.append(cur)
        p_max[0] = que[0]

        for i in range(N - K - 1):
            prev = P[i]
            cur = P[i + K + 1]
            if que[0] == prev:
                que.popleft()
            while que and cur > que[-1]:
                que.pop()
            que.append(cur)
            p_max[i + 1] = que[0]

    def calc_asc():
        prev = -1
        cnt = 0
        for i in range(K):
            cur = P[i]
            if prev < cur:
                cnt += 1
            else:
                cnt = 1
            prev = cur
        p_asc[0] = cnt

        for i in range(N - K):
            cur = P[i + K]
            if prev < cur:
                p_asc[i + 1] = min(p_asc[i] + 1, K)
            else:
                p_asc[i + 1] = 1
            prev = cur

    calc_min()
    calc_max()
    calc_asc()

    uf = UnionFind(N - K + 1)

    asc_list = []
    for i in range(N - K + 1):
        if p_asc[i] == K:
            asc_list.append(i)
    if len(asc_list) > 1:
        for i in range(1, len(asc_list)):
            uf.union(asc_list[0], asc_list[i])

    for i in range(N - K):
        if p_min[i] == P[i] and p_max[i] == P[i + K]:
            uf.union(i, i + 1)

    print(uf.group_count())


if __name__ == '__main__':
    main()
