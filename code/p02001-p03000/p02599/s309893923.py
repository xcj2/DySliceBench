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
    C = list(map(int, input().split()))
    query = []
    for q in range(Q):
        query.append(list(map(int, input().split())))
        query[-1].append(q)
    query.sort(key=lambda x: x[1])

    last = [0] * (N+1)
    for i, c in enumerate(C):
        if i > query[0][1]-1:
            break
        last[c] = i+1

    bit = Bit(N)
    for i in range(1, N+1):
        if last[i]:
            bit.add(last[i], 1)
    r_prev = query[0][1]
    ans = [0] * Q
    for l, r, q in query:
        if r > r_prev:
            for i in range(r_prev+1, r+1):
                j = last[C[i-1]]
                if j:
                    bit.add(j, -1)
                last[C[i-1]] = i
                bit.add(i, 1)
            r_prev = r
        ans[q] = bit.sum(r) - bit.sum(l-1)

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
