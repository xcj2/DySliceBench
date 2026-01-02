# ABC110d
import sys
from collections import Counter
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
MOD = 10**9+7


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


dp = dict()


def combinations_count(n, r):
    if dp.get(n) != None and dp.get(n).get(r) != None:
        return dp[n][r]
    if dp.get(n) == None:
        dp[n] = dict()
    dp[n].update({r: math.factorial(
        n) // (math.factorial(n - r) * math.factorial(r))})
    return dp[n][r]


def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)


ans = 1
pr = Counter(prime_factorize(m))
for i in pr.values():
    # print(i)
    t = combinations_count(n + i - 1, i)
    # print(t)
    ans = ans*t % MOD
# print(pr)
# print(len(pr))
print(ans)