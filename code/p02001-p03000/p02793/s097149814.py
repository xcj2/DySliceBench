from collections import defaultdict, Counter
import math
import fractions

MOD = 1000000007

N = int(input())
A = list(map(int, input().split()))

mod = 1000000007


def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]


def mod_inv(a):
    x = extgcd(a,MOD)[0]
    return (MOD+x%MOD)%MOD


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


all = Counter()
for i in range(N):
    li = prime_factorize(A[i])
    tmp = Counter(li)
    for k, v in tmp.items():
        if all[k] < v:
            all[k] = v

# print(all)
lsm = 1
for k, v in all.items():
    lsm = lsm*(k**v)%MOD
# print(lsm)

ans = 0
for i in range(N):
    ans = (ans + lsm * mod_inv(A[i])) % MOD

print(ans)