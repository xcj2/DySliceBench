import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7
M = 998244353


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def segfunc(x, y):
    return x + y


def main():
    N, K = map(int, readline().split())
    LR = list(list(map(int, readline().split())) for _ in range(K))
    LR.sort()

    A = [0] * (N + 1)
    A[1] = 1
    seg = SegTree(A, segfunc=segfunc, ide_ele=0)
    for i in range(2, N + 1):
        for l, r in LR:
            if i - l > 0:
                total = (seg.tree[i + seg.num] + seg.query(max(1, i - r), min(N, i - l + 1)) % M)
                seg.update(i, total)
            else:
                break
    print(seg.tree[seg.num + N] % M)


if __name__ == '__main__':
    main()
