import sys
input = sys.stdin.readline
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a//gcd(a, b)*b
    
def inv(x):
    return pow(x, MOD-2, MOD)
    

def factorize(n):
    factors = []
    
    for i in range(2, int(n**0.5)+1):
        cnt = 0
        
        while n%i==0:
            n //= i
            cnt += 1
    
        if cnt>0:
            factors.append((i, cnt))
    
    if n>1:
        factors.append((n, 1))
    
    return factors

N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7
#N = 10**4
#A = [i for i in range(10**6, 10**6-N, -1)]

L = 1
d = defaultdict(int)

for Ai in A:
    f = factorize(Ai)
    
    for n, c in f:
        d[n] = max(d[n], c)

for v, c in d.items():
    L *= v**c
    L %= MOD
    
ans = 0

for Ai in A:
    ans += L*inv(Ai)
    ans %= MOD

print(ans)