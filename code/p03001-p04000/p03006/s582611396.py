import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def YesNo(x): return 'Yes' if x else 'No'
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from itertools import product
from collections import Counter

def main():
    N = II()
    if N == 1:
        return 1
    XY = []
    for _ in range(N):
        XY.append(LI())
    cnt = Counter()
    for p0, p1 in product(XY, repeat=2):
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        if dx != 0 or dy != 0:
            cnt[(dx, dy)] += 1
    ans = N - max(cnt.values())
    return ans

print(main())