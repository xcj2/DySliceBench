def main():
    import sys
    input = sys.stdin.buffer.readline
    N, Q = map(int, input().split())
    *C, = map(int, input().split())

    last = [-1]*(N+1)
    P = [[] for _ in [0]*(N+1)]
    for i, c in enumerate(C):
        if last[c] != -1:
            P[last[c]].append(i+1)
        last[c] = i+1

    queries = [[] for _ in [0]*(N+1)]
    for i in range(Q):
        l, r = map(int, input().split())
        queries[l].append((r, i))

    class BIT():
        def __init__(self, n, x=1):
            self.n = n
            self.T = [0]*(n+1)

        def add(self, i, x):
            while i <= self.n:
                self.T[i] += x
                i += i & -i

        def lsum(self, i):
            ret = 0
            while i > 0:
                ret += self.T[i]
                i ^= i & -i
            return ret

    A = BIT(N)
    ans = [0]*Q
    for l in range(N, 0, -1):
        for cr in P[l]:
            A.add(cr, 1)
        for r, i in queries[l]:
            ans[i] = r-l+1-A.lsum(r)

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
