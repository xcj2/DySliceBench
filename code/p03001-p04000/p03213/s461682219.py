import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from collections import Counter

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

N = I()
d = defaultdict(int)

for i in range(2,N+1):
    c = Counter(prime_factorize(i))
    for k in c.keys():
        d[k] += c[k]

n2 = 0
n4 = 0
n14 = 0
n24 = 0
n74 = 0
for k in d.keys():
    if d[k]>=74:
        n74 += 1
    if d[k]>=24:
        n24 += 1
    if d[k]>=14:
        n14 += 1
    if d[k]>=4:
        n4 += 1
    if d[k]>=2:
        n2 += 1

ans = 0
if n4>=2 and n2>=3:
    ans += n4*(n4-1)//2 * (n2-2)
if n14>=1 and n4>=2:
    ans += n14*(n4-1)
if n24>=1 and n2>=2:
    ans += n24*(n2-1)
ans += n74

print(ans)