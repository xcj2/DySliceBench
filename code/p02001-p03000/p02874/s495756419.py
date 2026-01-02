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

from operator import itemgetter

n = ni()
lefts = []
rights = []
intervals = []
for _ in range(n):
    l, r = li()
    r += 1
    lefts.append(l)
    rights.append(r)
    intervals.append((l, r))

maxleft = max(lefts)
minright = min(rights)
ans = 0

## (1)最高の左端と最低の右端が同じ集合にあるとき
# 1区間のみを選択
longest = 0
for l, r in intervals:
    if l == maxleft or r == minright:
        continue
    else:
        longest = max(longest, r - l)
ans = longest + max(0, minright - maxleft)

## (2)最高の左端と最低の右端が別の集合にあるとき
intervals = sorted(sorted(intervals, key=itemgetter(1), reverse=True), key=itemgetter(0))

s_maxleft = [intervals[0][0]]
s_minright = [intervals[0][1]]
t_maxleft = [intervals[-1][0]]
t_minright = [intervals[-1][1]]

for idx, (l, r) in enumerate(intervals):
    if idx == 0:
        continue
    s_maxleft.append(max(s_maxleft[-1], l))
    s_minright.append(min(s_minright[-1], r))

for idx, (l, r) in enumerate(intervals[::-1]):
    if idx == 0:
        continue
    t_maxleft.append(max(s_maxleft[-1], l))
    t_minright.append(min(t_minright[-1], r))

t_maxleft = t_maxleft[::-1]
t_minright = t_minright[::-1]

for i in range(n-1):
    ans = max(ans, max(0, s_minright[i] - s_maxleft[i]) + max(0, t_minright[i+1] - t_maxleft[i+1]))

print(ans)
