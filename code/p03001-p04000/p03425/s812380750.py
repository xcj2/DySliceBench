from collections import defaultdict
from itertools import combinations
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
s = SR(n)
d = defaultdict(int)
for c in ['M', 'A', 'R', 'C', 'H']:
    d[c] = 0
for name in s:
    if name[0] in {'M', 'A', 'R', 'C', 'H'}:
        d[name[0]] += 1
combs = list(combinations(['M', 'A', 'R', 'C', 'H'], 3))

ans = 0
for c in combs:
    ans += d[c[0]] * d[c[1]] * d[c[2]]
print(ans)
