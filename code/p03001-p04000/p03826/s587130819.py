import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from collections import Counter
from itertools import product
from math import factorial

# prime numbers
primes = list(range(int(10**5) + 1))
primes[1] = 0
for i in range(2, int(len(primes) ** 0.5) + 1):
    if primes[i]:
        for j in range(2 * i, len(primes), i):
            primes[j] = 0

def main():
    A, B, C, D = LI()
    return max(A * B, C * D)

print(main())