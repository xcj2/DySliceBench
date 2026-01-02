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
    N, C = l_inpl()
    D = [ l_inpl() for _ in range(C) ]
    c = []
    for _ in range(N):
        ci = l_inpl()
        ci = [ i-1 for i in ci ] 
        c.append(ci)

    # t[i][j]: i={0, 1, 2}, jは色
    t = create_grid(3, C)
    for ci in range(C):
        for i in range(N):
            for j in range(N):
                t[(i+j)%3][ci] += D[c[i][j]][ci]

    ans = INF
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                tmp += t[0][i]
                tmp += t[1][j]
                tmp += t[2][k]
                ans = min(ans, tmp)
    
    print(ans)
if __name__ == "__main__":
    main()
