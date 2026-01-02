class fenwick_tree:
    """
    区間の一点更新と，区間和の取得がO(log n)で可能なデータ構造
    1-indexedで実装
    """

    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N+1)

    def init_array(self, A):
        for i, a in enumerate(A, start=1):
            self.add(i, a)

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


class fenwick_tree_RAQ_and_RSQ():
    """
    Range Add Queryと，Range Sum QueryがどちらもO(logn)
    BIT 2本使う
    1-indexed 半閉区間
    """

    def __init__(self, n):
        self.p = fenwick_tree(n+1)
        self.q = fenwick_tree(n+1)

    def init_array(self, A):
        for i, a in enumerate(A):
            pass

    def add_interval(self, i, j, w):
        """ [i,j]にwを加算 """
        j += 1
        self.p.add(i, -w*i)
        self.p.add(j, w*j)
        self.q.add(i, w)
        self.q.add(j, -w)

    def sum_until(self, i):
        """ [1,c)の和を求める """
        if i <= 0 or self.p.size < i:
            raise IndexError
        return self.p.sum_until(i) + self.q.sum_until(i)*(i)

    def sum_acc(self, i, j):
        """ [i,j] の区間和を取得 """
        return self.sum_until(j+1) - self.sum_until(i)


def main():
    N, Q = (int(i) for i in input().split())
    bit = fenwick_tree_RAQ_and_RSQ(N)
    for _ in range(Q):
        com, *A = (int(i) for i in input().split())
        if com == 0:
            (x, y, w) = A
            bit.add_interval(x, y, w)
        elif com == 2:
            x = A[0]
            print(bit.sum_until(x))
        else:
            x, y = A
            print(bit.sum_acc(x, y))


if __name__ == '__main__':
    main()

