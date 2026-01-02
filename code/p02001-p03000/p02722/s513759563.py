import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


def divisors(n, sort=False):
    """
    nの約数をO(√n)で列挙する
    """
    d = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    if sort:
        d.sort()
    return d


N = I()

ans = 0
for d in divisors(N - 1):
    if d > 1:
        ans += 1
for d in divisors(N):
    if d == 1:
        continue
    num = N
    while num % d == 0:
        num = num // d
    if num % d == 1:
        ans += 1
print(ans)

