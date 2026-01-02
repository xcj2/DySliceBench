import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from bisect import bisect_left
from itertools import accumulate

n = ni()
a = list(li())
b = list(li())

a_larger = []
lack = 0
ans = 0

# ai > bi のものを降順にならべ、累積和
# ai < bi のものは総和
for ai, bi in zip(a, b):
    if ai > bi:
        a_larger.append(ai - bi)
    elif ai < bi:
        lack += (bi - ai)
        ans += 1

a_larger.sort(reverse=True)
a_larger_cum = [0] + list(accumulate(a_larger))

# 二分探索
idx = bisect_left(a_larger_cum, lack)
if idx >= len(a_larger_cum):
    print(-1)
else:
    print(ans + idx)