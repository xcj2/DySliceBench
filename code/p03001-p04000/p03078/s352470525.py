import sys
#import numpy as np

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

N = 10000
def tokey(i, j, k):
    return i*N*N + j*N + k
def dekey(n):
    i = int(n / N / N)
    j = int(n / N) % N
    k = n % N
    return i, j, k

def main():
    X, Y, Z, K = i2nn()
    A = i2nn()
    B = i2nn()
    C = i2nn()
    A.sort()
    A.reverse()
    B.sort()
    B.reverse()
    C.sort()
    C.reverse()
    Q = [(A[0] + B[0] + C[0], 0, 0, 0)]
    loop = 0
    stored = set()
    def next(i, j, k):
        if i >= X or j >= Y or k >= Z:
            return
        key = tokey(i, j, k)
        if key not in stored:
            stored.add(key)
            n = A[i] + B[j] + C[k]
            Q.append((n, i, j, k))
    while True:
        Q.sort(key=lambda v: v[0])
        v = Q.pop()
        print(v[0])
        loop += 1
        if loop >= K:
            break
        next(v[1]+1, v[2], v[3])
        next(v[1], v[2]+1, v[3])
        next(v[1], v[2], v[3]+1)

main()
