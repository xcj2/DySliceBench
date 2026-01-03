from itertools import accumulate

class BIT:
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)

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
    N, K, *A = map(int, open(0).read().split())

    B = [0] + list(accumulate(a - K for a in A))

    memo = {n: i for i, n in enumerate(sorted(set(B)), 1)}
    bit = BIT(N + 1)

    ans = 0
    for b in map(memo.get, B):
        ans += bit.sum(b)
        bit.add(b, 1)

    print(ans)

if __name__ == '__main__':
    main()
