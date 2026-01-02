class BIT(object):
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)


def main():
    n = int(input())
    *a, = map(int, input().split())
    small, large = 0, max(a)
    criteria = n * (n + 1) // 4

    while large - small > 1:
        mid = (small + large) // 2
        num = 0
        b = BIT(2 * n + 1)
        suma = 0
        b.add(suma + n + 1, 1)
        for aa in a:
            suma += 1 if aa <= mid else -1
            num += b.sum(suma + n)
            b.add(suma + n + 1, 1)

        if num > criteria:
            large = mid
        else:
            small = mid
    print(large)


main()
