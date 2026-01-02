class fenwick_tree:
    """
    区間の一点更新と，区間和の取得がO(log n)で可能なデータ構造
    1-indexedで実装
    """

    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N+1)

    def sum_until(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def sum_acc(self, i, j):
        """ [i,j] の和を返す """
        return self.sum_until(j) - self.sum_until(i-1)

    def add(self, i, x):
        if i <= 0:
            return
        while i <= self.size:
            self.tree[i] += x
            i += i & (-i)


def main():
    N, Q = (int(i) for i in input().split())
    C = [int(i) for i in input().split()]
    Query = [[] for _ in range(N+1)]
    for j in range(Q):
        le, ri = (int(i) for i in input().split())
        Query[ri].append((le, j))

    Query.append((-1, -1, -1))

    lastappend = [-1] * (N + 1)
    bit = fenwick_tree(N)
    ans = [0]*Q

    for i, a in enumerate(C, start=1):
        if lastappend[a] != -1:
            bit.add(lastappend[a], -1)
        lastappend[a] = i
        bit.add(i, 1)
        for (le, j) in Query[i]:
            ri = i
            ans[j] = bit.sum_acc(le, ri)

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
