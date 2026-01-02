#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    mod = 998244353
    N, K = iim()
    it = map(int, sys.stdin.read().split())
    B = list(zip(it, it))

    N1 = N+1 if N&1 else N
    N2 = 1<<(N.bit_length())
    NN2 = N1 + N2
    A = [0] * NN2

    def add(a, i, j, x):
        i += N2; j += N2
        while i < j:
            if i & 1:
                A[i] = (A[i] + x) % mod
                i += 1
            if not j & 1:
                A[j] = (A[j] + x) % mod
                j -= 1
            i >>= 1; j >>= 1
        if i == j:
            A[i] = (A[i] + x) % mod

    def get(a, i):
        i += N2
        ans = 0
        while i > 0:
            ans = (ans + A[i]) % mod
            i >>= 1
        return ans

    A[N2] = 1

    B.sort()
    for i in range(N-1):
        x = get(A, i)
        for a, b in B:
            a += i; b += i
            if a > N-1: continue
            b = min(b, N-1)
            add(A, a, b, x)

    print(get(A, N-1))


if __name__ == "__main__":
    resolve()
