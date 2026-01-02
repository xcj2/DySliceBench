import bisect
from collections import Counter
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n, m = LI()
a = LI()
a = sorted(a)[::-1]
bc = LIR(m)
bc = sorted(bc, key=lambda x: x[1])[::-1]
all_c = []
for bi, ci in bc:
    all_c += [ci] * bi
    if len(all_c) >= n:
        break
if len(all_c) < n:
    all_c += [0] * (n - len(all_c))

ans = 0
a_i = 0
c_i = 0
for _ in range(n):
    if a[a_i] > all_c[c_i]:
        ans += a[a_i]
        a_i += 1
    else:
        ans += all_c[c_i]
        c_i += 1
print(ans)
