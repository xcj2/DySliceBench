import sys
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7

N, P = MI()
S = input()

if P == 2:
    ans = 0
    for i, c in enumerate(S):
        if int(c) % 2 == 0:
            ans += i + 1
    print(ans)
elif P == 5:
    ans = 0
    for i, c in enumerate(S):
        if c in ['5', '0']:
            ans += i + 1
    print(ans)
else:
    d = defaultdict(int)
    tenmod = 1
    lastmod = 0
    for i, c in enumerate(reversed(S)):
        if i > 0:
            tenmod = tenmod * 10 % P
        lastmod = (int(c) * tenmod % P + lastmod) % P
        d[lastmod] += 1
    ans = 0
    for m, cnt in d.items():
        if m == 0:
            ans += cnt
        ans += cnt * (cnt - 1) // 2
    print(ans)
