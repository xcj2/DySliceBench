#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    N, Q = iim()
    it = map(int, sys.stdin.read().split())

    M = N + 1if N & 1 else N
    NM = 1<<M.bit_length()
    ans = (N-2)**2
    A = [[N-2]*(NM+M) for i in range(2)]

    def set(a, i, j, x):
        i += NM; j += NM
        while i < j:
            a[i] = min(a[i], x)
            if i&1:
                i += 1
            a[j] = min(a[j], x)
            if j&1 == 0:
                j -= 1
            i >>= 1; j >>= 1
        a[i] = min(a[i], x)
    def get(a, i):
        i += NM
        ans = a[i]
        while i > 0:
            i >>= 1
            ans = min(ans, a[i])
        return ans

    for q, i in zip(it, it):
        q -= 1; i -= 2
        val = get(A[q], i)
        ans -= val
        set(A[q^1], 0, val, i)
    print(ans)


if __name__ == "__main__":
    resolve()
