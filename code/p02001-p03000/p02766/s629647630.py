import sys, os, math, bisect, itertools, collections, heapq, queue, copy, array

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
INF = float('inf')


def combinations_count(n, r, mod=MOD):
    def factorial_mod(N, mod=MOD):
        ret = 1
        for n in range(1, N + 1):
            ret *= n
            ret %= mod
        return ret

    q = factorial_mod(n + r, mod)
    b = factorial_mod(n, mod)
    d = factorial_mod(r, mod)
    b = pow(b, mod - 2, mod)
    d = pow(d, mod - 2, mod)
    return (q * b * d) % mod


def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, K = il()
    print(len(Base_10_to_n(N, K)))


if __name__ == '__main__':
    main()
