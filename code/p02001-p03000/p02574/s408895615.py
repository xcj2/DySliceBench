import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = 10**6
    table = [0 for _ in range(N+1)]
    prime = [True] * (N+1)
    for i in range(2, N+1):
        if not prime[i]:
            continue
        else:
            table[i] = i
            num = i + i
            while num < N:
                prime[num] = False
                table[num] = i
                num += i

    def factorize(n):
        ans = []
        while not prime[n]:
            ans.append(table[n])
            n = n // table[n]
        ans.append(n)
        return ans
    n = I()
    A = LI()
    coprime = True
    c = collections.Counter()
    memo = {}
    for a in A:
        soinsu = factorize(a)
        memo[a] = soinsu
        for s in soinsu:
            c[s] += 1
    for a in A:
        soinsu = memo[a]
        for s in soinsu:
            c[s] -= 1
        for s in soinsu:
            if s == 1:
                continue
            if c[s] > 0:
                coprime = False
                break
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    if coprime:
        print("pairwise coprime")
        return

    setwise = False
    m = A[0]
    for a in A[1:]:
        m = gcd(a, m)
    if m == 1:
        setwise = True

    if setwise:
        print("setwise coprime")
        return

    print("not coprime")
    return





main()

