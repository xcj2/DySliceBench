mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.buffer.readline

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

        def lower_bound(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.size.bit_length() - 1)
            while k:
                if x + k <= self.size and self.tree[x + k] < w:
                    w -= self.tree[x + k]
                    x += k
                k >>= 1
            return x + 1

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    bit = Bit(N)
    for i, a in enumerate(A):
        bit.add(i+1, a)
    for _ in range(Q):
        q, x, y = map(int, input().split())
        if q == 0:
            bit.add(x+1, y)
        else:
            print(bit.sum(y) - bit.sum(x))


if __name__ == '__main__':
    main()
