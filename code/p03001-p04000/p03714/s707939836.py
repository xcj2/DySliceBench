#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    x, y = LI()
    a = [1, 3, 5, 7, 8, 10, 12]
    b = [4, 6, 9, 11]
    c = [2]
    if x in a and y in a:
        print("Yes")
        return
    if x in b and y in b:
        print("Yes")
        return
    if x in c and y in c:
        print("Yes")
        return
    print("No")
    return

#B
def B():
    h, w = LI()
    print("#" * (w + 2))
    for _ in range(h):
        a = ["#"]
        for s in S():
            a.append(s)
        a.append("#")
        print("".join(a))
    print("#" * (w + 2))
    return

#C
def C():
    h, w = LI()
    ans = inf
    for i in range(1, h):
        ans = min(ans, max(i * w, (h - i) * (w // 2), (h - i) * (w - w // 2)) - min(i * w, (h - i) * (w // 2), (h - i) * (w - w // 2)))
        ans = min(ans, max(i * w, (h - i) // 2 * w, (h - i - (h - i) // 2) * w) - min(i * w, (h - i) // 2 * w, (h - i - (h - i) // 2) * w))
    h, w = w, h
    for i in range(1, h):
        ans = min(ans, max(i * w, (h - i) * (w // 2), (h - i) * (w - w // 2)) - min(i * w, (h - i) * (w // 2), (h - i) * (w - w // 2)))
        ans = min(ans, max(i * w, (h - i) // 2 * w, (h - i - (h - i) // 2) * w) - min(i * w, (h - i) // 2 * w, (h - i - (h - i) // 2) * w))
    print(ans)
    return

# D
# 解説AC
# ある点kにおいて2つに分けてa'の
# 前後半の要素を考える
# シンプルにわからなかった 
def D():
    n = II()
    a = LI()
    first_half_list = []
    final_half_list = []
    first_half_sum = deque([0])
    final_half_sum = deque([0])
    ans = -inf
    for i in range(n):
        heappush(first_half_list, a[i])
        first_half_sum[0] += a[i]
        heappush(final_half_list, -a[-i - 1])
        final_half_sum[0] -= a[-i - 1]
    for i in range(1, n + 1):
        q = heappop(first_half_list)
        heappush(first_half_list, max(q, a[i + n - 1]))
        first_half_sum.append(first_half_sum[-1] - q + max(q, a[i + n- 1]))
        q = heappop(final_half_list)
        heappush(final_half_list, max(q, -a[-n - i]))
        final_half_sum.appendleft(final_half_sum[0] - q + max(q, -a[-n - i]))
    for i in range(n + 1):
        ans = max(ans, first_half_sum[i] + final_half_sum[i])
    print(ans)
    return


#Solve
if __name__ == '__main__':
    D()
