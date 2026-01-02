from collections import Counter, defaultdict
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
a = LI()
c = Counter(a)
ans = 0
for i, count in c.items():
    if count == i:
        continue
    elif count > i:
        ans += count - i
    else:
        ans += count
print(ans)
