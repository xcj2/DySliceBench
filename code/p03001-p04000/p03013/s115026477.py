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
from bisect import bisect_left, bisect_right

# import numpy as np
# from scipy.special import perm
# from scipy.special import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

########

N, M = l_inpl()
a = { i_inpl(): True for _ in range(M)}
# for _ in range(M):
#     ai = i_inpl()
#     a.append(ai)

dp = [None] * (N+1)

dp[N] = 1
# print(dp)
for i in range(N-1, -1, -1):
    if i in a:
        dp[i] = 0
    else:
        if N-1 == i:
            dp[i] = 1
        else:
            if i+1 in a and i+2 in a:
                dp[i] = 0
            elif i+1 in a:
                dp[i] = dp[i+2]
            elif i+2 in a:
                dp[i] = dp[i+1]
            else:
                dp[i] = dp[i+1] + dp[i+2]

print(dp[0] % 1000000007)