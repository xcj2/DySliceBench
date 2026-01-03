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
# from scipy.special import perm
# from scipy.special import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

########

N, W = l_inpl()
w, v = [], []
item = [[] for i in range(4)]

for i in range(N):
    wi, vi = l_inpl()
    if i == 0:
        item[0].append(vi)
        w_base = wi
    else:
        item[wi - w_base].append(vi)

w0, w1, w2, w3 = item
w0 = [0] + list(accumulate(sorted(w0, reverse=True)))
w1 = [0] + list(accumulate(sorted(w1, reverse=True)))
w2 = [0] + list(accumulate(sorted(w2, reverse=True)))
w3 = [0] + list(accumulate(sorted(w3, reverse=True)))

ans = 0
for i in range(len(w0)):
    for j in range(len(w1)):
        for k in range(len(w2)):
            tmp_weight = w_base * i + (w_base + 1) * j + (w_base + 2) * k
            if tmp_weight > W:
                continue
            l = min((W - tmp_weight) // (w_base + 3), len(w3) - 1)
            tmp_ans = w0[i] + w1[j] + w2[k] + w3[l]
            ans = max(ans, tmp_ans)

print(ans)
