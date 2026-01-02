from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def PrimeFactorization(x):
    def plist(x):
        if x < 2: return []
        if x & 1 == 0: return [2] + plist(x >> 1)
        for p in range(3, x + 1, 2):
            if x % p == 0: return [p] + plist(x // p)
            if p ** 2 > x: return [x]

    pl = plist(x)
    pp, ee = [], []
    for p in pl:
        if not pp or p != pp[-1]:
            pp += [p]
            ee += [0]
        ee[-1] += 1
    return [(p, e) for p, e in zip(pp, ee)]

def gcd(a,b):
    while b:a,b=b,a%b
    return a

def main():
    a,b=MI()
    g=gcd(a,b)
    pe=PrimeFactorization(g)
    print(len(pe)+1)

main()