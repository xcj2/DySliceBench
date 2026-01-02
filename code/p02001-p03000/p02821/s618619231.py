#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))


#O(nlogn)
def f(x):
    cnt = 0
    for i in a:
        idx = bl(a,x-i)
        cnt += n - idx
        if cnt >= m:
            return True
    return False

n,m = LI()
a = LI()
a.sort()
ng,ok = 2*max(a)+1,2
#O(log(max(a)))
while ng - ok > 1:
    mid = (ng+ok) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

ans = 0
tmp = 0
b = [0] + list(accumulate(a))
#O(nlogn)
for i in a:
    idx = bl(a,ok-i)
    # i*(n-idx) := 左手で握手する人の幸福度(i)*左手で握手する回数(n-idx)
    # (b[-1] - b[idx]) := 右手で握手する人の幸福度の総和
    ans += i*(n - idx) + (b[-1] - b[idx])
    # tmp := 左手で握手する人を決めたときの右手で握手した人の数の総和 = ペアの総数
    tmp += n - idx

# ペアの数がm以上なら答えからペアの数がmになるよう最小のペアの幸福度(ok)を引く
ans = ans - (tmp - m)*ok
print(ans)
