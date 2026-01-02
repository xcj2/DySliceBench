from collections import Counter
from collections import deque
from functools import reduce
from pprint import pprint
import bisect
import copy
import fractions
import itertools
import math
import queue
import random
import sys
import time
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def IS(): return input()
def C(x): return Counter(x)
def GCD_LIST(numbers): return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers): return reduce(LCM, numbers)
def LCM(m, n): return (m * n // fractions.gcd(m, n))
def same(x, y): return bool(root(x) == root(y))
def root(x):
    if node[x] == x:
        return x
    else:
        node[x] = root(node[x])
        return node[x]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        return  # 結合不要
    if size[x] < size[y]:
        x, y = y, x
    node[y] = x
    size[x] += size[y]
def return_size(x):
    return size[root(x)]
    

n, m = MI()
ans = [0] * (m + 1)
bridge = [LI() for _ in range(m)]
# union-find
node = [i for i in range(n)]
size = [1 for i in range(n)]
# 辺を追加していない状態
ans[0] = (n * (n - 1)) // 2
i = 0 
for a, b in bridge[::-1]:
    if same(a - 1, b - 1):  # 辺を追加する以前のもともと連結であった
        ans[i + 1] = ans[i]
    else:
        ans[i + 1] = ans[i] - return_size(a - 1) * return_size(b - 1)
    unite(a - 1, b - 1)
    i += 1
for i in ans[:m][::-1]:
    print(i)
