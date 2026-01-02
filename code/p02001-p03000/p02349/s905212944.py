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


class fenwick_tree_interval_add(fenwick_tree):
    """
    区間加算と，一点取得がO(log n)
    区間和を求めるのは，区間の長さをkとして，O(k)
    """

    def __init__(self, n):
        super().__init__(n)

    def init_array(self, A):
        for i in range(self.size):
            if i != 0:
                self.__add(i+1, A[i] - A[i-1])
            else:
                self.__add(i+1, A[i])

    def add_interval(self, i, j, w):
        if i <= 0 or self.size < j or j < i:
            raise IndexError
        self.__add(i, w)
        if j < self.size:
            self.__add(j+1, -w)

    def get_val(self, i):
        if i <= 0 or self.size < i:
            raise IndexError
        return self.__sum_until(i)

    def __sum_until(self, i):
        return super().sum_until(i)

    def __add(self, i, x):
        super().add(i, x)


def main():
    N, Q = (int(i) for i in input().split())
    bit = fenwick_tree_interval_add(N)
    for _ in range(Q):
        com, *A = (int(i) for i in input().split())
        if com == 0:
            (x, y, w) = A
            bit.add_interval(x, y, w)
        else:
            x = A[0]
            print(bit.get_val(x))


if __name__ == '__main__':
    main()

