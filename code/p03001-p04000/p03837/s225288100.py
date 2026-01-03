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
from heapq import heappush, heappop

import re
# import numpy as np
# from scipy.misc import comb

# 再帰がやばいとき
import sys
sys.setrecursionlimit(10**9)

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

INF = int(1e30)
MOD = int(1e9)+7 # 10^9 + 7

# field[H][W]
def create_grid(H, W, value = 0):
    return [[ value for _ in range(W)] for _ in range(H)]

########

def solve(G):
    N = len(G)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G

def main():
    N, M = l_inpl()
    G = create_grid(N, N, INF)

    for i in range(N):
        G[i][i] = 0

    a, b, c = [], [], []
    for _ in range(M):
        ai, bi, ci = l_inpl()
        ai, bi = ai-1, bi-1
        a.append(ai)
        b.append(bi)
        c.append(ci)
        G[ai][bi] = ci
        G[bi][ai] = ci
    
    G = solve(G)

    ans = M
    for i in range(M):
        flag = False
        for j in range(N):
            if G[j][a[i]]+c[i] == G[b[i]][j]:
                flag = True
        if flag:
            ans -= 1
    
    print(ans)
if __name__ == "__main__":
    main()
