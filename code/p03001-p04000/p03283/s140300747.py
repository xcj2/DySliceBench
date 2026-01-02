import math
import copy
from operator import mul
from functools import reduce
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
# 一次元累積和
from itertools import accumulate
from bisect import bisect_left, bisect_right

import re
# import numpy as np
# from scipy.misc import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

INF = int(1e18)
MOD = int(1e9)+7 # 10^9 + 7

# W行H列, x[W][H]
def create_grid(W, H, value = 0):
    return [[ value for _ in range(H)] for _ in range(W)]

########
N, M, Q = l_inpl()

l, r = [], []
for _ in range(M):
    li, ri = l_inpl()
    l.append(li)
    r.append(ri)

p, q = [], []
for _ in range(Q):
    pi, qi = l_inpl()
    p.append(pi)
    q.append(qi)

s = create_grid(N+1, N+1)

for i in range(M):
    s[l[i]][r[i]] += 1

for hi in range(1, N+1):
    for wi in range(1, N+1):
        s[hi][wi] += s[hi-1][wi]
        s[hi][wi] += s[hi][wi-1]
        s[hi][wi] -= s[hi-1][wi-1]

for i in range(Q):
    pi, qi = p[i], q[i]
    print(s[qi][qi] - s[qi][pi-1] - s[pi-1][qi] + s[pi-1][pi-1])