import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, P = mapint()
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
from collections import Counter
c = Counter(prime_factorize(P))

ans = 1
for num, cnt in c.most_common():
    if cnt<N:
        break
    ans *= num**(cnt//N)
print(ans)
        