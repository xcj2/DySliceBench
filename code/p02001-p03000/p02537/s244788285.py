#!/usr/bin/env python3
class segtree:
    """
    segment tree
    value store as object type and get update function(merge_func) from outside

    Attributes
    ----------
    n : int
        Number of elements
    initialize_func : func
        function for initialization
    merge_func : func
        function for merge x and y to x(this merge is distruction update)

    Methods
    -------
    update(i, x)
        update tree[i] value to x
    get(a, b)
        get value from [a, b)
        include a but not include b, return a merged value
    """
    def __init__(self, n, initialize_func, merge_func):
        """
        Constructer(Initialize parameter in this class)

        Parameters
        ----------
        n : int
            Number of elements
        initialize_func : func
            function for initialization
        merge_func : func
            function for merge x and y to x(this merge is distruction update)
        """
        self.n = n
        self.initialize = initialize_func
        self.merge = merge_func
        n2 = 1  # n2はnより大きい2の冪数
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        self.tree = [initialize_func() for _ in range(n2 << 1)]

    def update(self, index, x):
        index += self.n2
        self.tree[index] = self.merge(self.tree[index], x)
        while index > 1:
            # (index ^ 1) はiと1の排他的論理和(XOR)
            x = self.merge(x, self.tree[index ^ 1])
            index >>= 1  # 右ビットシフトで親ノードのインデックスへ移動
            self.tree[index] = self.merge(self.tree[index], x)

    def get(self, a, b):
        result = self.initialize()
        q = [(1, 0, self.n2)]
        while q:
            k, left, right = q.pop()
            if a <= left and right <= b:
                result = self.merge(result, self.tree[k])
                continue
            m = (left + right) // 2
            k <<= 1
            if a < m and left < b:
                q.append((k, left, m))
            if a < right and left < m:
                q.append((k + 1, m, right))
        return result


def main():
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    max_A = 3 * 10 ** 5 + 1

    seg = segtree(max_A, lambda: 0, max)
    for a in A:
        next = seg.get(max(0, a - K), min(a + K + 1, max_A))
        seg.update(a, next + 1)
    print(seg.get(0, max_A))


if __name__ == '__main__':
    main()
