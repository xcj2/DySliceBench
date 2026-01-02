from math import floor, sqrt
from collections import Counter

MOD = 10 ** 9 + 7

# xを素因数分解する
def getPrimeFactor(x):
    ans = []
    for d in range(2, floor(sqrt(x)) + 1):
        while x % d == 0:
            ans.append(d)
            x //= d

    if x != 1:
        ans.append(x)

    return ans

# xのn乗（二分累乗法）
def power(x, n):
    ans = 1
    while n:
        if n % 2 == 1:
            ans = (ans * x) % MOD
        x = (x * x) % MOD
        n //= 2
    return ans


N, M = map(int, input().split())

PFs = getPrimeFactor(M)
cnt = Counter(PFs)

N2 = N
if len(cnt):
    N2 += max(cnt.values())

# facts[x]: xの階乗
facts = [1] + [0] * N2
for x in range(1, N2 + 1):
    facts[x] = (facts[x - 1] * x) % MOD

# invFs[x]: xの階乗の逆元
invFs = [0] * N2 + [power(facts[N2], MOD - 2)]
for x in reversed(range(N2)):
    invFs[x] = (invFs[x + 1] * (x + 1)) % MOD

def comb(n, k):
    return ((facts[n] * invFs[k]) % MOD * invFs[n - k]) % MOD


ans = 1
for num in cnt.values():
    ans = (ans * comb(N + num - 1, num)) % MOD
print(ans)
