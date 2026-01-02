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
    H, M = l_inpl()
    A = l_inpl()
    d = {
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6
    }

    new_d = {}
    for Ai in A:
        new_d[Ai] = d[str(Ai)]

    dp = [-INF] * (H+1) # ちょうどi本のマッチ棒を使って，条件を満たす整数を作るときの最大桁数
    dp[0] = 0

    for i in range(1, H+1):
        tmp = []
        for k, v in new_d.items():
            if i-v < 0:
                tmp.append(-INF)
            else:
                tmp.append(dp[i-v]+1)
        dp[i] = max(tmp)

    s = sorted(new_d.items(), key=lambda x:-x[0])

    ans = ""
    remain = H

    while remain > 0:
        for k, v in s:
            if remain >= v and dp[remain-v] != -INF and dp[remain-v] == dp[remain] - 1: # 一桁だけ減少している
                ans += str(k)
                remain -= v
                break
    print(ans)
if __name__ == "__main__":
    main()
