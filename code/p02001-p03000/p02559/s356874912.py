import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mat = lambda x, y, v: [[v]*y for _ in range(x)]
ten = lambda x, y, z, v: [mat(y, z, v) for _ in range(x)]
mod = 1000000007
sys.setrecursionlimit(1000000)

class BIT:
    def __init__(self, n):
        self.n = n
        self.nums = [0] * (n+1)
        
    def add(self, i, x):
        n, nums = self.n, self.nums
        i += 1
        while i <= n:
            nums[i] += x
            i += i & -i
    
    def sum(self, i):
        nums = self.nums
        s = 0
        i += 1
        while i:
            s += nums[i]
            i -= i & -i
        return s

N, Q = rl()
bit = BIT(N)
A = rl()
for i, a in enumerate(A):
    bit.add(i, a)
for i in range(Q):
    q = rl()
    if q[0] == 0:
        bit.add(q[1], q[2])
    else:
        print(bit.sum(q[2]-1) - bit.sum(q[1]-1))
