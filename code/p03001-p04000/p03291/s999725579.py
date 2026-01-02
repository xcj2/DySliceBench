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
# from scipy.misc import perm
# from scipy.misc import comb

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
INF = int(1e18)
MOD = int(1e9)+7 # 10^9 + 7

def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# dp[i][j]
def init_dp_table(i, j, init=INF):
  return [[ init for _ in range(j)] for _ in range(i)]

########

S = input()

dp = init_dp_table(len(S)+1, 4, 0)
dp[0][0] = 1

for i in range(len(S)):
    Si = S[i]
    if Si == "A" or Si == "?":
        dp[i+1][0] += dp[i][0] % MOD
        dp[i+1][1] += dp[i][1] % MOD
        dp[i+1][2] += dp[i][2] % MOD
        dp[i+1][3] += dp[i][3] % MOD
        dp[i+1][1] += dp[i][0] % MOD
    if Si == "B" or Si == "?":
        dp[i+1][0] += dp[i][0] % MOD
        dp[i+1][1] += dp[i][1] % MOD
        dp[i+1][2] += dp[i][2] % MOD
        dp[i+1][3] += dp[i][3] % MOD
        dp[i+1][2] += dp[i][1] % MOD
    if Si == "C" or Si == "?":
        dp[i+1][0] += dp[i][0] % MOD
        dp[i+1][1] += dp[i][1] % MOD
        dp[i+1][2] += dp[i][2] % MOD
        dp[i+1][3] += dp[i][3] % MOD
        dp[i+1][3] += dp[i][2] % MOD

print(dp[len(S)][3] % MOD)