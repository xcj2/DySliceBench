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

# import numpy as np
# from scipy.misc import perm
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

########

def main():
    A, B, Q = l_inpl()
    s = [-INF] + line_inpl(A) + [INF]
    t = [-INF] + line_inpl(B) + [INF]
    x = line_inpl(Q)

    for qi in range(Q):
        b, d = bisect_right(s, x[qi]), bisect_right(t, x[qi])
        res = INF
        for S in (s[b-1], s[b]):
            for T in (t[d-1], t[d]):
                d1, d2 = abs(S-x[qi]) + abs(T-S), abs(T-x[qi]) + abs(S-T)
                res = min(res, d1, d2)
        print(res)

if __name__ == "__main__":
    main()