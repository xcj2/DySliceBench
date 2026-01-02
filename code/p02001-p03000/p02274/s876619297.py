# Binary Indexed Tred
# https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree
# http://hos.ac/slides/20140319_bit.pdf
# https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree


from collections import defaultdict
import sys
input = sys.stdin.readline


class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 100)

    def add(self, i, x):
        i = i + 1
        while i <= self.size + 1:
            self.tree[i] += x
            i += i & -i
        return

    def sum(self, i):
        i = i + 1
        _sum = 0
        while i > 0:
            _sum += self.tree[i]
            i -= i & -i
        return _sum


def solve(n, A):
    ans = 0
    bit = FenwickTree(n)
    B = sorted(A)

    d = defaultdict(int)
    for i in range(n):
        d[B[i]] = i

    for i in range(n):
        t = A[i]
        ind = d[t] + 1
        ans += i - bit.sum(ind)
        bit.add(ind, 1)

    return ans


def main():
    n = int(input().strip())
    A = [int(i) for i in input().strip().split()]

    ans = solve(n, A)
    print(ans)


if __name__ == "__main__":
    main()
