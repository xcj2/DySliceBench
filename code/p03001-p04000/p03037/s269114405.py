# coding: utf-8
import sys
import itertools


def sr(): return sys.stdin.readline().rstrip()


def ir(): return int(sr())


def lr(): return list(map(int, sr().split()))


N, M = lr()
l_list = []
r_list = []
for i in range(M):
    l, r = lr()
    l_list.append(l)
    r_list.append(r)

# ans = set()
# left = l_list[M - 1]
# right = r_list[0]
tl_list = []
tr_list = []
for i in range(M):
    tmp_left = l_list[i]
    tmp_right = r_list[i]
    tl_list.append(tmp_left)
    tr_list.append(tmp_right)
left = max(tl_list)
right = min(tr_list)
# cards = sorted(l_list[i:] + r_list[:i + 1])
# cards = set(range(cards[0], cards[-1] + 1, 1))
# if (len(ans) == 0):
#     ans = cards
#     continue

# ans = cards & ans

ans = right - left + 1
if ans <= 0:
    print(0)
else:
    print(ans)
