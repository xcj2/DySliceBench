import sys
s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2sss = lambda n: [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def divisors(n):
    dd = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            dd.append(i)
            if i != n // i:
                dd.append(n//i)
    #dd.sort()
    return dd

def main():
    A, B, K = i2nn()
    g = gcd(A, B)
    dd = divisors(g)
    dd.sort()
    dd.reverse()
    n = dd[K-1]
    print(n)

main()
