import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i, x=1):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get_sum(self, i):
        i += 1
        x = 0
        while i > 0:
            x += self.data[i]
            i -= i & -i
        return x

    # Return sum for [l, r)
    def get_sum_range(self, l, r):
        return self.get_sum(r - 1) - self.get_sum(l - 1)


def main():
    N, Q = map(int, readline().split())
    C = list(map(int, readline().split()))
    LR = map(int, read().split())

    prev = [-1] * (N + 1)
    ps = [[] for _ in range(N)]
    for i, c in enumerate(C):
        if prev[c] != -1:
            ps[prev[c]].append(i)
        prev[c] = i

    qs = [[] for _ in range(N)]
    for i, (l, r) in enumerate(zip(*[iter(LR)] * 2)):
        qs[l - 1].append((r - 1, i))

    ans = [0] * Q
    bit = BIT(N)

    for l in range(N - 1, -1, -1):
        for r in ps[l]:
            bit.add(r)
        for r, i in qs[l]:
            ans[i] = (r - l + 1) - bit.get_sum(r)

    print('\n'.join(map(str, ans)), sep='\n')

    return


if __name__ == '__main__':
    main()
