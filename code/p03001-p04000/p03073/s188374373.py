import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def POW(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return POW(x, y // 2) ** 2 % MOD
    else:
        return POW(x, y // 2) ** 2 * x % MOD
def mod_factorial(x, y): return x * POW(y, MOD - 2) % MOD
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from collections import Counter

# prime numbers
_nprime = 10 ** 5 + 1
primes = list(range(int(_nprime) + 1))
primes[1] = 0
for i in range(2, int((_nprime + 1) ** 0.5) + 1):
    if primes[i]:
        for j in range(2 * i, _nprime + 1, i):
            primes[j] = 0

def main():
    S = SI()
    ans = [0, 0]
    i = 0
    for s in S:
        if int(s) == i:
            ans[0] += 1
        else:
            ans[1] += 1
        i = 1 - i
    ans = min(ans)
    return ans

print(main())
