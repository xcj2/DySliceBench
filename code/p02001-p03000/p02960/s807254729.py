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

# field[H][W]
def create_grid(H, W, value = 0):
    return [[ value for _ in range(W)] for _ in range(H)]

########

S = input()
N = len(S)

# dp[i][k]: i桁目までのkで割った余りの数
dp = create_grid(N+1, 13)

dp[0][0] = 1 # 0桁目

s = [1]
for i in range(N):
  s.append((s[-1]*10)%13)

for i in range(N):
    c = S[N-i-1]
    if c == "?":
        v = range(10)
    else:
        v = [int(c)]
    for vi in v:
        for j in range(13):
            amari = (vi*s[i] + j) % 13
            dp[i+1][amari] = (dp[i][j] + dp[i+1][amari]) % MOD

print(dp[N][5])

