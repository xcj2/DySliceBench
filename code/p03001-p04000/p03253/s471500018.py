MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  itertools import permutations

def sieve(n):
    prime = []
    limit = n ** 0.5
    data = [i + 1 for i in range(1,n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e%p != 0]

def Factor(n,primes):
    factor = {}
    for p in primes:
        while n%p == 0:
            n //= p
            if p in factor:
                factor[p] += 1
            else:
                factor[p] = 1
    
    if n != 1:
        factor[n] = 1
    
    return factor

MAXN = 110000
factorial = [1]
for i in range(1, MAXN + 1):
    factorial.append(factorial[-1] * i % MOD)

inv_factorial = [-1] * (MAXN + 1)
inv_factorial[-1] = pow(factorial[-1], MOD-2, MOD)
for i in reversed(range(MAXN)):
    inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

def fact(n):
    return factorial[n]

def nck(n, k):
    if k>n or k<0:
        return 0
    else:
        return factorial[n] * inv_factorial[n-k] * inv_factorial[k]

def main():
    n,m = map(int,input().split())
    primes = sieve(100000)
    factor = Factor(m,primes)

    ans = 1
    for v in factor.values():
        ans *= nck(v + n - 1,v)
        ans %= MOD
    
    print(ans)

if __name__ =='__main__':
    main()  