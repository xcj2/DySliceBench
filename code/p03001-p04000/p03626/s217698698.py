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

INF = int(1e18)
MOD = int(1e9)+7 # 10^9 + 7

# field[H][W]
def create_grid(H, W, value = 0):
    return [[ value for _ in range(W)] for _ in range(H)]

########

def main():
    N = i_inpl()
    S1, S2 = input(), input()

    l = []
    i = 0
    while True:
        if S1[i] == S2[i]:
            l.append("X")
        else:
            l.append("Y")
            i += 1
        i += 1
        if i >= N:
            break

    if l[0] == "X":
        ans = 3
    else:
        ans = 6

    for i in range(1, len(l)):
        if l[i-1] == "X" and l[i] == "Y":
            ans *= 2
        elif l[i-1] == "X" and l[i] == "X":
            ans *= 2
        elif l[i-1] == "Y" and l[i] == "Y":
            ans *= 3
        elif l[i-1] == "X" and l[i] == "Y":
            ans *= 1
        ans %= MOD

    print(ans)
if __name__ == "__main__":
    main()
