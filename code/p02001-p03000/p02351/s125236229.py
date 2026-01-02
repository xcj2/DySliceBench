import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class BinaryIndexTree:  # 1-indexed
    def __init__(self, N):
        """
        INPUT
        N [int] -> 全部0で初期化
        N [list] -> そのまま初期化
        """
        if isinstance(N, int):
            self.N = N
            self.depth = N.bit_length()
            self.tree = [0] * (N + 1)
            self.elem = [0] * (N + 1)
        elif isinstance(N, list):
            self.N = len(N)
            self.depth = self.N.bit_length()
            self.tree = [0] + N
            self.elem = [0] + N
            self._init()
        else:
            raise "INVALID INPUT: input must be int or list"

    def _init(self):
        size = self.N + 1
        for i in range(1, self.N):
            if i + (i & -i) > size:
                continue
            self.tree[i + (i & -i)] += self.tree[i]

    def add(self, i, x):
        self.elem[i] += x
        while i <= self.N:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def lower_bound(self, val):
        if val <= 0:
            return 0
        i = 0
        k = 1 << self.depth
        while k:
            if i + k <= self.N and self.tree[i + k] < val:
                val -= self.tree[i + k]
                i += k
            k >>= 1
        return i + 1

    def upper_bound(self, val):
        if val < 0:
            return 0
        i = 0
        k = 1 << self.depth
        while k:
            if i + k <= self.N and self.tree[i + k] <= val:
                val -= self.tree[i + k]
                i += k
            k >>= 1
        return i + 1


class RangeSumAdd:
    def __init__(self, N):
        self.bit0 = BinaryIndexTree(N)
        self.bit1 = BinaryIndexTree(N)

    def RangeAdd(self, l, r, x):
        """
        閉区間[l, r]にxを加える
        """
        self.bit0.add(l, -x * (l - 1))
        self.bit0.add(r + 1, x * r)
        self.bit1.add(l, x)
        self.bit1.add(r + 1, -x)

    def getSum(self, i):
        return self.bit0.sum(i) + i * self.bit1.sum(i)

    def RangeSum(self, l, r):
        """
        閉区間[l, r]にxを加える
        """
        return self.getSum(r)-self.getSum(l-1)


if __name__ == "__main__":
    N, Q = map(int, input().split())
    bit = RangeSumAdd(N + 10)
    ans = []

    for _ in range(Q):
        T, *arg = map(int, input().split())
        if T == 0:
            bit.RangeAdd(*arg)
        else:
            ans.append(bit.RangeSum(*arg))

    if ans:
        print(*ans, sep="\n")

