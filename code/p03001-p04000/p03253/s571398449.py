import math
import collections

#Max = 210000
Mod = 1000000007
"""
fac = [0] * Max
finv = [0] * Max
inv = [0] * Max
def COMinit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, Max):
        fac[i] = fac[i-1] * i % Mod 
        inv[i] = Mod - inv[Mod%i] * (Mod//i) % Mod
        finv[i] = finv[i-1] * inv[i] % Mod """
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
def COMinit():
    for i in range(2, N+111):
        fac.append(fac[-1]*i%Mod)
        inv.append((-inv[Mod%i] * (Mod//i)) % Mod)
        finv.append(finv[-1] * inv[-1] % Mod)
    

def COM(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % Mod) % Mod

N, M = map(int, input().split())
prime_count = collections.Counter()
for i in range(2, math.ceil(math.sqrt(M))+1):
    while M % i == 0:
        M /= i
        prime_count[i] += 1
if M > 1:
    prime_count[M] += 1

ans = 1
COMinit()
for i, b in prime_count.items():
    tmp = COM(b+N-1, N-1)
    ans = (ans * tmp) % Mod 
print(ans)
