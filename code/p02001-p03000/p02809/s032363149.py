from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


class BIT:
    def __init__(self, size):
        self.bit = [0] * size
        self.size = size
        self.total = 0

    def add(self, i, w):
        x = i + 1
        self.total += w
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        res = 0
        x = i + 1
        while x:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def search(self, k):
        if k > self.total:
            return -1
        if k == 0:
            return 0
        step = 1 << (self.size.bit_length() - 1)
        now_index = 0
        ret = 0
        while step:
            if now_index + step < self.size and ret + self.bit[now_index + step - 1] < k:
                ret += self.bit[now_index + step - 1]
                now_index += step
            step >>= 1
        # now_indexを伸ばしいって、sumがk以上に達する直前まで伸ばし続けるならreturnのところでnow_index - 1。
        # その場合、bit.sum(now_index - 1) <= k < bit.sum(now_index)
        # 達してすぐのindexであれば-1しない
        return now_index


n = I()
A = LI()
if n == 2:
    if A[0] == 2 and A[1] == 1:
        print(-1)
    elif A[0] != 2:
        print(1, 2)
    else:
        print(2, 1)
    exit()


bit  = BIT(n + 1)
for i in range(1, n + 1):
    bit.add(i, 1)


ans = []
pre = -1
for j in range(n - 1):
    x = bit.search(1)
    if x == pre:
        x = bit.search(2)
    bit.add(x, -1)
    ans += [x]
    pre = A[x - 1]

last_x = bit.search(1)
bit.add(last_x, -1)
if A[ans[-1] - 1] != last_x:
    ans += [last_x]
    print(*ans)
    exit()


cnt = 0
for k in range(n - 2, -1, -1):
    if A[ans[k] - 1] == last_x:
        x = ans.pop()
        bit.add(x, 1)
        cnt += 1
    else:
        break


if cnt == 1:
    last3 = []
    for a, b, c in permutations((ans.pop(), x, last_x)):
        if A[ans[-1] - 1] != a and A[a - 1] != b and A[b - 1] != c:
            last3 += [[a, b, c]]
    print(*ans + min(last3))
    exit()


ans += [last_x]
x = bit.search(1)
if x == A[ans[-1] - 1]:
    x = bit.search(2)
bit.add(x, -1)
ans += [x]
for l in range(cnt - 1):
    x = bit.search(1)
    bit.add(x, -1)
    ans += [x]
print(*ans)
