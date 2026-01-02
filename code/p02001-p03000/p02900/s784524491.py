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
     
def integer_factorization(n):
    prime_count = collections.Counter()
    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n //= i
            prime_count[i] += 1
    if n > 1:
        prime_count[n] += 1
    return prime_count

def main():
    a, b = LI()
    d1 = integer_factorization(a)
    d2 = integer_factorization(b)
    dk1 = [k for k, v in d1.items()]
    dk2 = [k for k, v in d2.items()]
    ans = set()
    for a in dk1:
        if d2[a] == 0:
            continue
        ans.add(a)

    for b in dk2:
        if d1[b] == 0:
            continue
        ans.add(b)

    print(1 + len(ans))


main()

