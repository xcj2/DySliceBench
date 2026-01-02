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

from collections import defaultdict
from bisect import bisect_left

n, k = li()
a = list(li())

a = a + a

# ジャンプ先
jump = defaultdict(lambda: -1)
buf = defaultdict(lambda: -1)
for i, ai in enumerate(a):
    if buf[ai] != -1:
        jump[buf[ai]] = i - buf[ai]

    buf[ai] = i

# 周期を求める
checkpoint = [0]
cur = 0

while cur == 0 or cur % n > 0:
    cur += jump[cur % n]
    cur += 1
    checkpoint.append(cur)

cycle = cur // n
mod = k % cycle

# あまり処理
if mod == 0:
    print()

else:
    last_idx = n * mod

    # シミュレーション
    start_idx = checkpoint[bisect_left(checkpoint, last_idx) - 1]
    s = []

    idx = start_idx
    while idx < last_idx:
        if idx + jump[idx % n] < last_idx:
            idx += jump[idx % n] + 1
        else:
            s.append(a[idx % n])
            idx += 1

    print(*s)
