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


def integer_factorization_perm(N):
    prime_count = collections.Counter()
    for n in range(1, N+1):
        for i in range(2, int(math.sqrt(n)) + 2):
            while n % i == 0:
                n //= i
                prime_count[i] += 1
        if n > 1:
            prime_count[n] += 1
    return prime_count

def main():
    N = I()
    primes = integer_factorization_perm(N)
    over74, over24, over14, over4, over2 = 0, 0, 0, 0, 0
    for k, v in primes.items():
        if v >= 74:
            over74 += 1
        if v >= 24:
            over24 += 1
        if v >= 14:
            over14 += 1
        if v >= 4:
            over4 += 1
        if v >= 2:
            over2 += 1
    cnt = 0
    '''
    print('74: ', over74)
    print('24: ', over24)
    print('14: ', over14)
    print('4: ', over4)
    print('2: ', over2)
    '''

    cnt += over74
    if over2 > 1:
        cnt += over24 * (over2 - 1)
    if over4 > 1:
        cnt += over14 * (over4 - 1)
    if over2 > 1 and over4 > 0:
        cnt += (over2 - 2) * over4 * (over4 - 1) // 2
    print(cnt)

main()
