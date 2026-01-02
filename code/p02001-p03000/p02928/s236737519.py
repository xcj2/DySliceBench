# jsc2019-qualB - Kleene Inversion
class BIT:  # Binary Indexed Tree (Fenwick Tree)
    def __init__(self, lim):
        self.size = lim
        self.tree = [0] * (lim + 1)  # 1-idx

    def add(self, i, x):  # add x to tree[i], O(logN)
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):  # sum of [1, i], O(logN)
        ret = 0
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    def range_sum(self, l, r):  # range sum of [l, r]
        return self.sum(r) - self.sum(l - 1)


def main():
    N, K = tuple(map(int, input().split()))
    A = tuple(map(int, input().split()))
    MOD = 10 ** 9 + 7
    bit = BIT(2000)
    x = 0
    for i, a in enumerate(A, 1):  # internal inversion
        bit.add(a, 1)
        x += i - bit.sum(a)
    y = -x
    for i, a in enumerate(A, 1):  # external inversion
        bit.add(a, 1)
        y += i + N - bit.sum(a)
    ans = (x * K + y * K * (K - 1) // 2) % MOD
    print(ans)


if __name__ == "__main__":
    main()