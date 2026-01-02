import sys
from bisect import bisect_left

MOD = 998244353
input = sys.stdin.readline


class SegmentTree():
    def __init__(self, values, merge_func=min, default=float("inf")):
        n = len(values)
        self.size = 1
        self.default = default
        self.merge = merge_func
        while self.size < n:
            self.size *= 2
        # tree[0] = empty
        # child of tree[n] = tree[n*2], tree[n*2+1]
        self.tree = [self.default] * self.size * 2
        self.range = [None] * self.size * 2
        for i in range(n):
            self.tree[self.size + i] = values[i]
        for i in range(self.size):
            self.range[self.size + i] = (i, i+1)
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.merge(self.tree[i*2], self.tree[i*2+1])
            self.range[i] = (self.range[i*2][0], self.range[i*2+1][1])

    def get(self, index):
        return self.tree[self.size + index]

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.merge(
                self.tree[index*2], self.tree[index*2+1])

    # query segmentation value of [a, b)
    def query(self, a, b):
        q = [1]
        ret = self.default
        while len(q):
            k = q.pop()
            l, r = self.range[k]
            if r <= a or b <= l:
                continue
            if a <= l and r <= b:
                ret = self.merge(ret, self.tree[k])
            else:
                q.append(k*2)
                q.append(k*2+1)
        return ret


def main():
    N = int(input())
    robo = [None] * N
    for i in range(N):
        robo[i] = tuple(map(int, input().split()))
    robo.sort()
    pos = [x[0] for x in robo]
    dst = [x[0] + x[1] for x in robo]
    rmq = SegmentTree(dst, max, -float("inf"))
    for i in range(N-1)[::-1]:
        dst[i] = rmq.query(i, bisect_left(pos, dst[i]))
        rmq.update(i, dst[i])

    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(N):
        x, d = robo[N-1-i]
        to = N - bisect_left(pos, dst[N-1-i])
        dp[i+1] = (dp[i] + dp[to]) % MOD
    print(dp[N])


if __name__ == "__main__":
    main()
