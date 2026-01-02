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

# 再帰がやばいとき
# import sys
# sys.setrecursionlimit(10**9)

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

INF = int(1e50)
MOD = int(1e9)+7 # 10^9 + 7

# field[H][W]
def create_grid(H, W, value = 0):
    return [[ value for _ in range(W)] for _ in range(H)]

########

def main():
    H, W, K = l_inpl()
    dp = create_grid(H+1, W)
    for i in range(W):
        dp[0][i] = 0
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            for k in range(0, 2**(W-1)): # 引ける横線の数
                ok = True
                for l in range(W-2):
                    if (k >> l) & 1 and (k >> (l+1)) & 1:
                        # 隣に線が引かれている
                        ok = False
                if not ok:
                    continue
                if j > 0 and (k >> (j-1)) & 1:
                    # jの左に横線が引かれるケース
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= MOD
                elif j < W-1 and (k >> j) & 1:
                    # jの右側に横線が引かれるケース
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= MOD
                else:
                    # jの両側に横線が引かれないケース
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= MOD

    print(dp[H][K-1])

if __name__ == "__main__":
    main()
