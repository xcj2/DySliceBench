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

N = i_inpl()
A = l_inpl()
B = l_inpl()

ans = 0

for i in range(N):
    if B[i] >= A[i]:
        ans += A[i]
        diff = B[i] - A[i]
        if diff >= A[i+1]:
            ans += A[i+1]
            A[i+1] = 0
        else:
            ans += diff
            A[i+1] -= diff
    else:
        ans += B[i]

print(ans)
# N = i_inpl()
# p = l_inpl()

# l = list(range(1, N+1))

# cnt = 0
# for pi, li in zip(p, l):
#     if pi != li:
#         cnt += 1

# if cnt == 2 or cnt == 0:
#     print("YES")
# else:
#     print("NO")