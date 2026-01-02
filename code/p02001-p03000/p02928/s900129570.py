MOD = 10 ** 9 + 7


def MAP():
    return list(map(int, input().split()))


class BinaryIndexedTree:
    def __init__(self, tree_size):
        self.tree_size = tree_size
        self.tree = [0] * (self.tree_size + 1)

    def add(self, i, x):
        while 0 < i <= self.tree_size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while 0 < i:
            s += self.tree[i]
            i -= i & -i
        return s


def count_inversion(A, max_num):
    bit = BinaryIndexedTree(max_num)
    x = 0
    for i, a in enumerate(A, start=1):
        bit.add(a, 1)
        x += i - bit.sum(a)
    return x


def main():
    N, K = MAP()
    A = MAP()

    tento_int = count_inversion(A, 2000)  # Aの内部で発生する転倒数
    tento_ext = count_inversion(sorted(A, reverse=True), 2000)  # AiとAjの間で発生する転倒数

    x = tento_int * K
    y = tento_ext * K * (K - 1) // 2
    print((x + y) % MOD)


if __name__ == "__main__":
    main()
