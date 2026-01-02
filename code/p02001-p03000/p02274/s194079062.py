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


def main():
    N = int(input())
    *A, = map(int, input().split())

    compress_dict = {x: i for i, x in enumerate(sorted(set(A)), start=1)}
    M = len(compress_dict)

    bit = Bit(M)
    ans = 0
    for cnt, x in enumerate(A, start=1):
        x = compress_dict[x]
        bit.add(x, 1)
        ans += cnt - bit.sum(x)

    print(ans)


if __name__ == '__main__':
    main()

