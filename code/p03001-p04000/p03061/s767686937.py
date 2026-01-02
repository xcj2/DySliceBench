# AtCoder Beginner Contest 125
# https://atcoder.jp/contests/abc125
import sys

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in list(ss)]
ss2nnn = lambda ss: [s2nn(s) for s in list(ss)]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline() for _ in range(n)]
ii2nnn = lambda n: ss2nnn(ii2ss(n))

cache = {}


def gcd(a, b):
    if a not in cache:
        cache[a] = {}
    if b in cache[a]:
        return cache[a][b]
    if b == 0:
        cache[a][b] = a
        return a
    n = gcd(b, a % b)
    cache[a][b] = n
    return n

def main_lte(N, An):
    if N == 2:
        n = max(An[0], An[1])
        print(n)
        return
    nn = [An[0]] * N
    nn[0] = An[1]
    for i in range(1, N):
        for j in range(N):
            if i == j:
                continue
            nn[j] = gcd(nn[j], An[i])
    print(int(max(nn)))

def main(N, An):
    if N == 2:
        n = max(An[0], An[1])
        print(n)
        return
    nn0 = gcd(An[0], An[1])
    nn1 = set((An[0], An[1]))
    for i in range(2, N):
        t1 = nn0
        nn0 = gcd(nn0, An[i])
        t2 = [gcd(n, An[i]) for n in nn1]
        nn1 = set(t2)
        nn1.add(t1)
    n = max(nn1)
    print(int(n))

N = i2n()
An = i2nn()
main(N, An)
