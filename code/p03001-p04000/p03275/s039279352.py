def d_median_of_medians(N, A):
    class BIT(object):
        """Binary Indexed Tree (1-indexed)"""

        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, index):
            """tree[1]からtree[index]までの和を計算"""
            ret = 0
            while index > 0:
                ret += self.tree[index]
                index -= index & (-index)
            return ret

        def add(self, index, value):
            """tree[index]にvalueを加算"""
            while index <= self.size:
                self.tree[index] += value
                index += index & (-index)

    def is_accepted(x):
        """
        A[l]からA[r]までの要素の中央値がx以上か。すなわち、A[l]からA[r]までの
        要素のうちx以上であるものが (N*(N+1)/2)/2 個以上か
        """
        from itertools import accumulate
        from math import ceil
        a_larger_x = [(1 if a >= x else -1) for a in A]  # x以上か否かを{1, -1}に変換
        cumsum = list(accumulate(a_larger_x))

        ans = 0
        a_larger_x_sorted = {a: k for k, a in enumerate(sorted(cumsum), 1)}
        bit = BIT(N)
        for c in cumsum:
            ans += bit.sum(a_larger_x_sorted[c]) + int(c >= 0)
            bit.add(a_larger_x_sorted[c], 1)
        return True if ans >= ceil((N * (N + 1)) / 4) else False

    # 二分探索の探索区間は [min(A), max(A)] で十分だが、
    # min, maxはO(N)なので、決め打ちしたほうがNが大きなとき速い
    accept = 0
    reject = 10**9 + 1  # 数列の要素の値の制約から、この値は中央値になりえない
    while reject - accept > 1:
        mid = (accept + reject) // 2
        if is_accepted(mid):
            accept = mid
        else:
            reject = mid
    return accept

N = int(input())
A = [int(i) for i in input().split()]
print(d_median_of_medians(N, A))